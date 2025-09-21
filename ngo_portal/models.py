from django.db import models
from django.contrib.auth.models import User

# NGO creates events
class NGOEvent(models.Model):
    ngo = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.title

# Volunteers apply for events
class VolunteerApplication(models.Model):
    event = models.ForeignKey(NGOEvent, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE)
    motivation = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.volunteer.username} → {self.event.title}"

