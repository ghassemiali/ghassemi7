from django.shortcuts import render
from blog.models import Post, Tag

def home_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    return render(request, 'website/contact.html')

def elements_view(request):
    return render(request, 'website/elements.html')

def test_view(request):
    temp_dict = {'fname': 'Ali', 'lname': 'Ghassemi'}
    return render(request, 'test.html', temp_dict)