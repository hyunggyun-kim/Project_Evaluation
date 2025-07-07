from django.db import models

# Create your models here.
class Project(models.Model):
    project = models.CharField(max_length=100)
    explain = models.TextField()

    def average(self):
        stars = self.stars.all()
        if stars.exists():
            return round(sum(st.score for st in stars) / stars.count(), 1)
        return 0

    def __str__(self):
        return self.project

class Star(models.Model):
    projectname = models.ForeignKey(Project, related_name='stars', on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i,i) for i in range (1,6)])

    def __str__(self):
        return f"{self.projectname.project} - {self.score}점"
