# for email or google apps
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
with open('./Skycision/email.config') as f:
    EMAIL_HOST_USER = f.readline().strip()
    EMAIL_HOST_PASSWORD = f.readline().strip()
EMAIL_PORT = 587