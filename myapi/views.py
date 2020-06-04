from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import wikipedia


# Create your views here.
class Summary(APIView):

    def get(self, request):
        text = request.headers['text']
        return Response(wikipedia.summary(text))
