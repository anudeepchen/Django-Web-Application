from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Skycision.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    # Home page
    url(r'^$', 'Skycision.views.home', name='home'),
    
    # Contact page
    url(r'^contact/', 'contact.views.contact', name='contact'),
    
    # Log in
    url(r'^accounts/login/$', 'login.views.login'),
    url(r'^accounts/userinfo/$', 'login.views.userinfo'),
    
    #url(r'^accounts/enter_email/$', 'login.views.enter_email'),
    url(r'^accounts/new_password/$', 'login.views.new_password'),
    url(r'^accounts/set_password/$', 'login.views.set_password'),
    url(r'^accounts/auth/$', 'login.views.auth_view'),
    url(r'^accounts/logout/$', 'login.views.logout'),
    url(r'^accounts/loggedin/$', 'login.views.loggedin'),
    
    # Register
    url(r'^accounts/register/$', 'register.views.register'),
    url(r'^accounts/register_user/$', 'register.views.register_user'),  
    
    # File Upload
    url(r'^accounts/upload/$', 'upload.views.upload'), 
    url(r'^accounts/upload_file/$', 'upload.views.upload_file'),
    
    #Password_Reset
    url(r'^accounts/forgot_password/$', 'login.views.forgot_password'),
    url(r'^accounts/enter_email/$', 'login.views.enter_email'),
    url(r'^accounts/new_password/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'login.views.login'),
    # Admin page
    url(r'^admin/', include(admin.site.urls)),
)

# Static files pattern
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

