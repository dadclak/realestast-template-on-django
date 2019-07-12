from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    newsBlock = NewsBlock.objects.filter(show=True)
    return render(request, 'realestast/index.html', {'news': newsBlock})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            recipients = ['kozan4in97@ya.ru']
            info = {"success": True, "info": ''}
            try:
                send_mail("Message from contact form",
                        "\nName: %s"
                        "\nE-mail: %s"
                        "\nPhone: %s"
                        "\nMessage: %s"
                        % (name, email, phone, message),
                        'kozanchyn.vladeo@gmail.com', recipients
                )
                info["info"] = 'Successful! We get your message!'
            except BadHeaderError:
                info["info"] = 'You have a small problem!'
                info["success"] = False
                return HttpResponse('Invalid header found')
            return render(request, 'realestast/contact.html', {'info': info})
    else:
        form = ContactForm()
        return render(request, 'realestast/contact.html', {'form': form})