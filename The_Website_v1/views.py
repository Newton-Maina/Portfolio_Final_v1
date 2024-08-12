from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Service, Project, ProjectDetail, Post
from django.core.mail import send_mail, BadHeaderError
from socket import gaierror
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic


# Create your views here.
def index(request):
    return render(request, 'index.html', {'navbar': 'home'})


def about(request):
    return render(request, 'about.html', {'navbar': 'about'})


def service(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'navbar': 'services', 'services': services})


def portfolio(request):
    projects_list = Project.objects.all().order_by('id')
    paginator = Paginator(projects_list, 3)

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


def project_detail_layout(request):
    return render(request, 'detailings/project-detail-layout.html')


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_detail, created = ProjectDetail.objects.get_or_create(project=project)

    previous_project = Project.objects.filter(pk__lt=pk).order_by('-pk').first()
    next_project = Project.objects.filter(pk__gt=pk).order_by('pk').first()

    return render(request, 'detailings/project-detail.html', {'project': project,
                                                              'project_detail': project_detail,
                                                              'previous_project': previous_project,
                                                              'next_project': next_project})


def handle_url_existence(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_detail, created = ProjectDetail.objects.get_or_create(project=project)

    if not project_detail.live_url:
        return render(request, 'detailings/404-error.html', status=404)

    return HttpResponseRedirect(project_detail.live_url)


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog-index.html'
    context_object_name = 'posts'
    paginate_by = 3


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/blog-detail.html'
