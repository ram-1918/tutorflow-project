from django.db import models
from users.models import Users


class Questions(models.Model):
    userid = models.ForeignKey(Users, on_delete=models.CASCADE)
    question = models.TextField(blank=True, unique=True)
    is_closed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.question