# views.py
from django.shortcuts import render
from .forms import MultipleEmailsForm
from .finderEngine import check_url
from django.http import HttpResponse
from .models import EmailModel
from .serializers import EmailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import csv

def process_multiple_emails(email_list):
    # Process each email in the list
    emails = [email.strip() for email in email_list.split(',')]
    return emails

def save_emails_to_model(email_list):
    # Join the email addresses into a comma-separated string
    all_emails = ', '.join(email_list)

    # Create a single instance of EmailModel
    instance = EmailModel(emails=all_emails)
    
    # Save the instance to the database
    instance.save()

    return instance

def download_csv(emails):
    # Create a CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="emails.csv"'

    # Create a CSV writer and write the header
    writer = csv.writer(response)
    writer.writerow(['Email Address'])

    # Write each email address to the CSV file
    for email in emails:
        print(f"The emails is {email}")
        writer.writerow([email])

    return response

@api_view(['GET', 'POST'])
def web_form_view(request):
    if request.method == 'POST':
        form = MultipleEmailsForm(request.data)  # Use request.data for API requests
        if form.is_valid():
            web_list = form.cleaned_data['email_list']
            updated_webs = process_multiple_emails(web_list)
            final_email = check_url(updated_webs)
            saved_email = save_emails_to_model(final_email)
            serializer = EmailSerializer(instance=saved_email)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

    return Response(data={'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

def download_emails(request):
    # Get the email data from the context
    emails = request.GET.getlist('emails')

    # Download CSV
    return download_csv(emails)
