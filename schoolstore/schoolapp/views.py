from django.contrib import messages, auth

from django.shortcuts import render, redirect

# Create your views here.
def home(request):

   return  render(request,"index.html")


def userhome(request):

   return  render(request,"userhome.html")