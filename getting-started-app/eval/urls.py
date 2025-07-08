from django.urls import path
from .views import ProjectList, ProjectDetail, ProjectAverage

urlpatterns = [
    path('', ProjectList.as_view(), name='project_list'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project_detail'),
    path('projects/<int:pk>/average/', ProjectAverage.as_view(), name='average'),
]   