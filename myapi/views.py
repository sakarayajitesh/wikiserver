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
            print(textList.strip('][').split(","))
            responseList = []
            for text in list(textList.strip('][').split(",")):
                print("requesting = ", text)
                try:
                    response = wikipedia.summary(str(text), sentences=3)
                    responseList.append({"text": text, "result": response})
                except Exception as e:
                    print(e)
            return Response(responseList)
        except Exception as e:
            print(str(e))
            return Response(str(e), 500)
