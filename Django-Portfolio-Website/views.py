from django.shortcuts import render
from datetime import datetime
from home.models import Contact

def index(requests):
  return render(requests, "index.html")

def about(requests):
  return render(requests, "about.html")

def contact(requests):
  if requests.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    desc = request.POST.get('desc')
    contact = Contact(name=name, email=email, desc=desc)
    contact.save()



  
  return render(requests, "contact.html")

  

