from django.shortcuts import render 
from home.models import Contact
from datetime import datetime

# Create your views here.
def index (request):
    return render (request , 'index.html')

def services (request):
    return render (request , 'services.html')


def contact (request):
    if request.method == "POST":
        name = request.POST.get ("name")
        phone = request.POST.get ("phone")
        age = request.POST.get ("age")
        birth = request.POST.get ("birth")
        location = request.POST.get ("location")
        # tickettype = request.POST.get ("tickettype")
        # quantity= request.POST.get ("quantity")

        contact = Contact (name=name , phone=phone , age=age , birth=birth , location=location , date = datetime.today ())
        contact.save ()
    
    return render (request , 'contact.html')