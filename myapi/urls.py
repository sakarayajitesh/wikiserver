from django.urls import path
from . import views

urlpatterns = [
    path('summary/', views.Summary.as_view()),
]