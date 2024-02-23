from .serializers import EmailSerializer, SortingSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from .finderEngine import get_email
from .sortingEngine import sortingInput
from .models import FinderModel, SortingModel
import re

def process_multiple_input(input_text):
    # Process the input text for conversion into list
    processedInput = [output.strip() for output in re.split(r'[,\t*\s]+', input_text)]
    return processedInput

@method_decorator(csrf_exempt, name='dispatch')
class WebFormView(generics.ListCreateAPIView):
    
    queryset = FinderModel.objects.all()
    serializer_class = EmailSerializer

    def perform_create(self, serializer):
        allEmail = []
        website_name = self.request.data['web_list']
        listed = process_multiple_input(website_name)
        scrappedEmail = get_email(listed)

        # Save the scraped emails to the database
        for email in scrappedEmail:
            allEmail.append(email)
            serializer.save(emails=allEmail, web_list=website_name)

        return Response(data={"Message" : "Succesfully done"}, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class SortFormView(generics.ListCreateAPIView):

    queryset = SortingModel.objects.all()
    serializer_class = SortingSerializer

    def perform_create(self, serializer):
        allSorted = []
        inputText = self.request.data['email']
        listedInput = process_multiple_input(inputText)
        sortedInput = sortingInput(listedInput)

        # Save the sorted data to the database
        for sorted in sortedInput:
            allSorted.append(sorted)
            serializer.save(email=allSorted)

        return Response(data={"Message" : "Succesfully done"}, status=status.HTTP_200_OK)

class EmailSenderView():
    pass

