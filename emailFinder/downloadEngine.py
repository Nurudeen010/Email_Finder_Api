# views.py
from django.http import HttpResponse
import csv

def download_emails(request, emails):
    # Dummy list of email addresses for demonstration purposes
    #emails = ["john@example.com", "jane@example.com", "bob@example.com"]

    # Create a CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="emails.csv"'

    # Create a CSV writer and write the header
    writer = csv.writer(response)
    writer.writerow(['Email Address'])

    # Write each email address to the CSV file
    for email in emails:
        writer.writerow([email])

    return response
