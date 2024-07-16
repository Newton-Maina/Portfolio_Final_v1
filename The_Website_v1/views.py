from django.shortcuts import render
from .models import Service, Project
from django.core.mail import send_mail, BadHeaderError
from socket import gaierror
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    return render(request, 'index.html', {'navbar': 'home'})


def about(request):
    return render(request, 'about.html', {'navbar': 'about'})


def service(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'navbar': 'services', 'services': services})


def portfolio(request):
    projects_list = Project.objects.all()  # Fetch all projects
    paginator = Paginator(projects_list, 3)  # Adjust as needed

    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'portfolio.html', {'navbar': 'portfolio', 'page_obj': page_obj})


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        if name and email and subject and message:
            try:
                # Send email
                send_mail(
                    f'Message from {name}',
                    f'Senders Email: {email} -- Details on message: {message}',
                    email,
                    ['newtonmainag@gmail.com'],
                )
                # Display success message in the same template
                return render(request, 'contact.html',
                              {'success_message': 'Your message has been sent successfully.', 'name': name})

            except BadHeaderError:
                error_message = "Invalid header found on your email."
                return render(request, 'contact.html', {'error_message': error_message, 'navbar': 'contact'})

            except gaierror:
                error_message = ("OOPS!! Sorry! Network error: Unable to send your message. Please check your internet "
                                 "connection and try again.")
                return render(request, 'contact.html', {'error_message': error_message, 'navbar': 'contact'})

            except Exception as e:
                error_message = f"An unexpected error occurred: {str(e)}"
                return render(request, 'contact.html', {'error_message': error_message, 'navbar': 'contact'})

        else:
            # Handle form validation errors
            error_message = "Please fill out all required fields."
            return render(request, 'contact.html', {'error_message': error_message, 'navbar': 'contact'})

    else:
        return render(request, 'contact.html', {'navbar': 'contact'})
