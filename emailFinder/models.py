from django.db import models

# Create your models here.
class FinderModel(models.Model):
    web_list = models.TextField()
    emails = models.TextField(blank=True)  # Use TextField to store multiple email addresses

    def get_email_list(self):
        # Return a list of email addresses
        return [email.strip() for email in self.emails.split(',')]