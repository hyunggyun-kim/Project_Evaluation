from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Project, Star

# Create your views here.
class ProjectList(ListView):
    model = Project
    template_name = 'eval/project_list.html'
    context_object_name = 'projects'
    ordering = ['project']

class ProjectDetail(DetailView):
    model = Project
    template_name = 'eval/project_detail.html'
    context_object_name = 'project'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        score = int(request.POST.get('score', 0))
        if 1<= score <= 5:
            Star.objects.create(projectname=self.object, score=score)
        return redirect('average', pk=self.object.pk)

class ProjectAverage(DetailView):
    model = Project
    template_name = 'eval/average.html'
    context_object_name = 'project'