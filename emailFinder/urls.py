# urls.py
from django.urls import path
from .views import WebFormView, download_emails

urlpatterns = [
    #path('email-form/', email_form_view, name='email_form_view_url'),
    path('download-emails/', download_emails, name='download_emails'),
    path('API/', WebFormView.as_view(), name='API'),
    # Add other URLs as needed
]
