from django.contrib import admin
from .models import Project, Star
from django.db.models import Avg

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project', 'explain', 'average_score')

    def average_score(self, obj):
        return obj.average()
    
    average_score.short_description = '평균 점수'
    average_score.admin_order_field = 'average_sort_key'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(average_sort_key=Avg('stars__score'))
    