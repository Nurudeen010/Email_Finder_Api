# urls.py
from django.urls import path
from .views import WebFormView

urlpatterns = [
    #path('email-form/', email_form_view, name='email_form_view_url'),

    path('API/', WebFormView.as_view(), name='API'),
    # Add other URLs as needed
]
