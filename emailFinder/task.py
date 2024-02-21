# tasks.py in your app
from celery import shared_task
import requests
import re
from itertools import chain

@shared_task
def get_emails(urls):
    email_address = []

    for url in urls:
        response = requests.get(url)

        if response.status_code == 200:
            html_content = response.text
            email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
            email_match = re.findall(email_pattern, html_content)
            if email_match:
                email_address.append(email_match)

    updated_email = list(set(chain(*email_address)))
    return updated_email
