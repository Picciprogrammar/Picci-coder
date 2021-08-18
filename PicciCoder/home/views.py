from django.shortcuts import render,HttpResponse
from .models import Contact

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")

        content = request.POST.get('content',"")
        content = Contact(name=name, email=email, content=content)
        content.save()
        
        
    return render(request, "home/contact.html")

    


