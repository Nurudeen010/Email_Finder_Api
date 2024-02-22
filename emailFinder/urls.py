# urls.py
from django.urls import path
from .views import WebFormView, SortFormView

urlpatterns = [
    #path('email-form/', email_form_view, name='email_form_view_url'),

    path('scrapperApi/', WebFormView.as_view(), name='scrapperAPI'),
    path('sortApi/', SortFormView.as_view(), name='sortAPI' )
    # Add other URLs as needed
]
