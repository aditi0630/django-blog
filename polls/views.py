from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.frode

def index(request):
	return HttpResponse("Hello")