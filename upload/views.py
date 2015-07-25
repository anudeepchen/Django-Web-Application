from .forms import DocumentForm
from .models import Document
from django.core.context_processors import csrf
from django.contrib import messages
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import mimetypes
from django.conf import settings
# Create your views here.

# Allows the user to upload the file
def upload(request):
    context = {}
    context.update(csrf(request))
    template = "upload.html"
    return render_to_response(template, context) 


# Method allows the  user to upload the file upon authentication
def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            #instance = Document(docfile=request.FILES['docfile'])
            file = request.FILES['docfile']
            print(file)
            filename = file.name
            store_in_s3(filename,file)
            print('filename')
            p=Document(url = "http://skycision.s3.amazonaws.com/" + filename)
            p.save()
            return HttpResponseRedirect('/accounts/login')
        else :
            messages.error(request, "dude something is wrong") 
    else:
        form = DocumentForm()
        messages.error(request, "dude something is wrong outside")
    context = {"form" :form}
    template = "upload.html"
    return render_to_response(template, context_instance = RequestContext(request,locals()))

#Method connects to S3 and stores the files into amazon s3
def store_in_s3(filename,content):
    try:
        conn = S3Connection(settings.ACCESS_KEY,settings.SECRET_ACCESS_KEY)
        b = conn.create_bucket("skycision")
        mime = mimetypes.guess_type(filename)[0]
        k = Key(b)       
        k.key = filename
        k.set_metadata("Content_Type",mime)      
        k.set_contents_from_file(content)
        k.set_acl('public-read')       
        print(k)
    except Exception :
        print (Exception)
        