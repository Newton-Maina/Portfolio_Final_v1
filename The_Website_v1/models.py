from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=200)
    case_name = models.CharField(max_length=200)
    description = models.TextField()
    image01 = models.ImageField(upload_to='images/', default="More Content Will Be Added Soon")
    image1 = models.ImageField(upload_to='images/', default="More Content Will Be Added Soon")
    image2 = models.ImageField(upload_to='images/', default="More Content Will Be Added Soon")
    image3 = models.ImageField(upload_to='images/', default="More Content Will Be Added Soon")

    def __str__(self):
        return self.title


class ProjectDetail(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    overview = models.TextField(default="More Content Will Be Added Soon")
    detail_paragraph1 = models.TextField(default="More Content Will Be Added Soon")
    detail_paragraph2 = models.TextField(default="More Content Will Be Added Soon")
    detail_paragraph3 = models.TextField(default="More Content Will Be Added Soon")
    detail_paragraph4 = models.TextField(default="More Content Will Be Added Soon")
    laptop_mockup = models.ImageField(upload_to='images/', default="More Content Will Be Added Soon")
    phone_mockup_01 = models.ImageField(upload_to='images/', default="More Content Will Be Added Soon")
    phone_mockup_02 = models.ImageField(upload_to='images/', default="More Content Will Be Added Soon")
    tech1 = models.CharField(max_length=200, default="Tech/You")
    tech2 = models.CharField(max_length=200, default="Tech/You")
    tech3 = models.CharField(max_length=200, default="Tech/You")
    tech4 = models.CharField(max_length=200, default="Tech/You")
    image4 = models.ImageField(upload_to='images/', default="More Content Will Be Added Soon")
    image5 = models.ImageField(upload_to='images/', default="More Content Will Be Added Soon")
    image6 = models.ImageField(upload_to='images/', default="More Content Will Be Added Soon")
    test_data = models.TextField(default="More Content Will Be Added Soon")
    live_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Details for {self.project.title}"


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.name


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title
