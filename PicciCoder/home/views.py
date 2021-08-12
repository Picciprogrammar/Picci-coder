from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def Contact(request):
    return render(request, 'home/contact.html')
