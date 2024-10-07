from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Location(models.Model):
    address = models.TextField()
    
    project = models.OneToOneField(
        'Project', 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='location',
    )

    def __str__(self) -> str:
        return self.address


class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    def __str__(self) -> str:
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=100)

    projects = models.ManyToManyField('Project', related_name='tags')

    def __str__(self) -> str:
        return self.name