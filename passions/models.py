from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.


class Passion(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("passion_list", kwargs={"pk": self.pk})


class Goal(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    target_start_date = models.DateField()
    target_finish_date = models.DateField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    passion = models.ForeignKey(Passion, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("goal_list", kwargs={"pk": self.pk})
