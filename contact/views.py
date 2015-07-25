from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import os

def sendemail(form):
    # get the data from the form
    first_name = form['first_name'].value()
    last_name = form['last_name'].value()
    email = form['email'].value()
    phone = form['phone'].value()
    interest = form['interest'].value()
    message = form['message'].value()
            
    # send email to Skycision support
    subject = "Someone contact us on Skycision.com"
    message = "Name: " + first_name + " " + last_name + "\n" + "Email: " + email + "\n" + "Phone: " + phone + "\n" + "Interest: " + interest + "\n" + "Message: " + message
    send_mail(subject, message,'contact.skycision@gmail.com', ['brendancarroll12@gmail.com'], fail_silently=False)

# Contact View
def contact(request):
    
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # save the form to the database
            save_it = form.save(commit=False)
            save_it.save()
            
            # send email 
            sendemail(form)
            
            # reset the form
            form = ContactForm()
            
            messages.success(request, "Accepted")
        else:
            messages.error(request, "Rejected")
    else:
        form = ContactForm()
    
    return render_to_response("contact.html", locals(), context_instance=RequestContext(request))