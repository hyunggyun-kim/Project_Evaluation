from django.shortcuts import render
from django.views.generic import ListView
from .models import Project

# Create your views here.
class ProjectList(ListView):
    model = Project
    template_name = 'eval/projectlist.html'
    context_object_name = 'projects'
    ordering = ['project']