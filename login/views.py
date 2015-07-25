#from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password,check_password
from .models import FailedLogin,UserInformation
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from datetime import datetime,timezone,timedelta
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.utils.timezone import utc,make_aware
import pytz
import datetime
from register.models import Register
from django.utils.encoding import force_bytes
from django.utils.html import format_html, format_html_join
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
# Create your views here.

#Method fetches the Ip of the user for authentication
def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for :
        ip = x_forwarded_for.split(',')[0]
    else :
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Method calculates the time between each failed login to determine when to lock the user's account
def time_tracker(request):
    user_ip = get_user_ip(request)
    email = request.POST.get('email','')
    try:
        first = FailedLogin.objects.filter(email=email,ipaddr = user_ip)
        diff_min = (datetime.datetime.now(timezone.utc)-first[0].timestamp).seconds/60
        if diff_min > 5 :
            FailedLogin.objects.filter(email=email,ipaddr = user_ip).delete()	
            Register.objects.filter(email=email).update(acc_locked = False)
            return True
        else : return False
    except FailedLogin.DoesNotExist:
        return True
    
# Method locks the user account for providing invalid credentails more than 3 times within 5 minutes
def acc_lockout(request):
    user_ip = get_user_ip(request)
    email = request.POST.get('email','')
    new_form = FailedLogin(email=email,timestamp = datetime.datetime.now(),ipaddr = user_ip)
    new_form.save()
    rec_count = FailedLogin.objects.filter(email=email,ipaddr = user_ip).count()
    print(rec_count)
    if rec_count >= 3 :
        Register.objects.filter(email=email).update(acc_locked = True)
        return "I'm sorry your account is locked, please check back after 5 minutes"

#Method checks if the user account is locked
def check_acc_lockout(email):
    user = Register.objects.get(email=email)
    print("user_account",user.acc_locked)
    if user.acc_locked :
        return True
    else : return False

# Login page
def login(request):
    c = {}
    request.session['last_activity'] = datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")
    dude = request.session['last_activity']
    print(dude)
    c.update(csrf(request))
    return render_to_response('login.html',c)


# Method verifies if the user provided credentails are invalid or not
def auth_view(request):
    email = request.POST.get('email','')
    password = request.POST.get('password','')
    print("expiry age",request.session.get_expiry_age())
    try:
        user = Register.objects.get(email = email)
        acc_lock = check_acc_lockout(email)
        if acc_lock :
            time_lapse = time_tracker(request)
            if time_lapse :
                messages.warning(request,"I'm sorry your account is locked, please check back after 5 minutes.")
        else :
            checkpwd = check_password(password,user.password)
            request.session['member_username'] = user.username             
            if checkpwd :
                request.session['old_post'] = request.POST
                #request.session['last_activity'] = json.dumps(datetime.now(), cls=DjangoJSONEncoder)
                #request.session['last_activity'] = datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")
                #print(json.dumps(datetime.now(), cls=DjangoJSONEncoder))
                dude = request.session['last_activity']
                #request.session.save()
                print(dude)
                return HttpResponseRedirect('/accounts/loggedin')  
            else :
                message = acc_lockout(request)
                if message is not None :
                    messages.error(request, message) 
                else :
                    messages.error(request, "Username/Password doesn't match. Please try again!") 
    except Register.DoesNotExist:
        acc_lockout(request)
        messages.error(request, "Email address doesn't exist!")        
    return render_to_response("login.html", locals(), context_instance=RequestContext(request))


def loggedin(request):
    return render_to_response('loggedin.html',{'full_name':request.user.username})

def logout(request):
    
    #if reques.session['last_activity'] is None:
    #    messages.error(request,"Logged out due to inactivity")
    if request.session.get_expiry_age() < 10 :
        messages.error(request,"Logged out due to inactivity")   
    try:
        del request.session['member_id']
        #del request.session['last_activity']
    except KeyError:
        pass
    return render_to_response('logout.html')


# Method is invoked when user clicks 'Forgot Password'
def forgot_password(request):
    context = {}
    context.update(csrf(request))
    template = "forgot_password.html"
    return render_to_response(template, context) 

# Method verifies if the user is authenticate and sends a email to user allowing him to change the password
def enter_email(request):
    if request.method == 'POST':        
        email = request.POST.get('email','')
        print(email)
        user = Register.objects.get(email = email)
        print(user.first_name)
        if user is not None:
            context ={
                 'email': user.email,
                        'domain': 'example.com', #or your domain
                        'site_name': 'example',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': '',
                        'user': user,                      
                        'protocol': 'http',}
            rendered = render_to_string('password_reset_email.html',context)
            send_mail('change password', rendered,'contact.skycision@gmail.com', ['achennup@andrew.cmu.edu'],fail_silently=False)
            return HttpResponseRedirect('/accounts/login')
        else : return HttpResponseRedirect('/accounts/invalid')
    else:
        return HttpResponseRedirect('/accounts/invalid')


# New Password
def new_password(request):
    context = {}
    context.update(csrf(request))
    template = "new_password.html"
    return render_to_response(template, context)  
    
# Method allows user to the change the password    
def set_password(request):
    print(request.method)
    if request.method == 'POST':
        password1 = request.POST.get('newpassword','')
        password2 = request.POST.get('confirmpassword','')
        if password1 == password2 :
            password = make_password(password1,salt = None,hasher = 'bcrypt_sha256')
            user = Register.objects.get(email = email)
            if user is not None :
                user.password = password
                user.save()
                return HttpResponseRedirect('/accounts/login')
            else : return HttpResponseRedirect('/accounts/invalid')
        else : return HttpResponseRedirect('/accounts/invalid')
    else : return HttpResponseRedirect('/accounts/invalid')
    
    
#User Information
def userinfo(request):
    old_post = request.session.get('old_post')
    print(make_aware(datetime.datetime.now()) - datetime.datetime.strptime(request.session['last_activity'],"%Y-%d-%m %H:%M:%S").replace(tzinfo=timezone.utc))
    if((make_aware(datetime.datetime.now()) - datetime.datetime.strptime(request.session['last_activity'],"%Y-%d-%m %H:%M:%S").replace(tzinfo=timezone.utc) > datetime.timedelta(0.00347222222))):
    #if request.session.get_expiry_age() <= 10:
        print("dude")
        logout(request)
    else:
        #request.session['last_activity'] = datetime.now()
        user = Register.objects.get(email = old_post['email'])
        context = {"first_name" : user.first_name,"last_name" : user.last_name}
        context.update(csrf(request))
        template = "userinfo.html"
        return render_to_response(template,context,context_instance = RequestContext(request,locals()))