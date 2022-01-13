from django.shortcuts import render
from blog.models import Post, Tag
from website.models import Contact
from website.forms import NameForm
from django.http import HttpResponse

def home_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    return render(request, 'website/contact.html')

def elements_view(request):
    return render(request, 'website/elements.html')

def test_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(name, subject, email, message)
        else:
            return HttpResponse('not valid')

    form = NameForm()
    return render(request, 'test.html', {'form': form})