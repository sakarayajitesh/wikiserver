from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import wikipedia
import json


# Create your views here.
class Summary(APIView):

    def get(self, request):
        try:
            textList = request.headers['textlist']
            responseList = []
            for text in json.loads(textList):
                print("requesting = ", text)
                try:
                    response = wikipedia.summary(text, sentences=3)
                    responseList.append({"text": text, "result": response})
                except Exception as e:
                    print(e)
            return Response(responseList)
        except Exception as e:
            print(e)
