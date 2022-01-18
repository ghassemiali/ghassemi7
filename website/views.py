from django.shortcuts import render
from blog.models import Post, Tag
from website.models import Contact
from website.forms import NameForm, ContactForm
from django.http import HttpResponse

def home_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('the data is not valid')
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def elements_view(request):
    return render(request, 'website/elements.html')

def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse('not valid')

    form = ContactForm()
    return render(request, 'test.html', {'form': form})