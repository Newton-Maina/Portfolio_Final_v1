from django.shortcuts import render, redirect
from .models import Service
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'index.html',{'navbar': 'home'})

def about(request):
    return render(request, 'about.html',{'navbar': 'about'})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html',{'navbar': 'services', 'services': services})

def portfolio(request):
    return render(request, 'portfolio.html',{'navbar': 'portfolio'})


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        if name and email and subject and message:
            # Send email
            send_mail(
                f'Message from {name}',
                f'Senders Email: {email} '
                f' -- Details on message: {message}',
                email,
                ['newtonmainag@gmail.com'],
            )

            # Display success message in the same template
            return render(request, 'contact.html', {'success_message': 'Your message has been sent successfully.', 'name': name})



        else:
            # Handle form validation errors
            error_message = "Please fill out all required fields."
            return render(request, 'contact.html', {'error_message': error_message, 'navbar': 'contact'})


    else:
        return render(request, 'contact.html', {'navbar': 'contact'})
