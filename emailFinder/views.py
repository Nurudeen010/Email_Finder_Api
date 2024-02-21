# views.py
#from .finderEngine import get_email
from .task import get_emails
from .models import FinderModel
from .serializers import EmailSerializer
from rest_framework.response import Response
from rest_framework import status, generics

def process_multiple_emails(web_list):
    # Process each email in the list
    url_name = [url.strip() for url in web_list.split(',')]
    return url_name

class WebFormView(generics.ListCreateAPIView):
    
    queryset = FinderModel.objects.all()
    serializer_class = EmailSerializer

    def perform_create(self, serializer):
        allEmail = []
        website_name = self.request.data['web_list']
        listed = process_multiple_emails(website_name)
        scrappedEmail = get_emails(listed)

        # Save the scraped emails to the database
        for email in scrappedEmail:
            allEmail.append(email)
            serializer.save(emails=allEmail, web_list=website_name)

        return Response(data={"Message" : "Succesfully done"}, status=status.HTTP_200_OK)
