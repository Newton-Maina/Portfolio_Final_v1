from django.contrib import admin

from .models import Service, Project, ProjectDetail, Post

# Register your models here.

admin.site.register(Service)
admin.site.register(Project)
admin.site.register(ProjectDetail)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title' 'content']


admin.site.register(Post, PostAdmin)
