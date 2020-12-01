from django.shortcuts import render
from .models import Project

def home(request):
    website = Project.objects.all()
    return render(request, 'portfolio/home.html',{'joni':website})

# Create your views here.
