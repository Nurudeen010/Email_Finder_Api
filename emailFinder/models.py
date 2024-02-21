from django.db import models

# Create your models here.
class WebsiteModel(models.Model):
    email_list = models.TextField()

class EmailModel(models.Model):
    emails = models.TextField(blank=True)  # Use TextField to store multiple email addresses

    def get_email_list(self):
        # Return a list of email addresses
        return [email.strip() for email in self.emails.split(',')]