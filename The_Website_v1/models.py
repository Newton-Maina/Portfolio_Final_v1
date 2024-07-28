from django.db import models


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


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.name
