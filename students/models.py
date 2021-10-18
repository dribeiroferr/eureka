from django.db import models


class Student(models.Model):
    first_name = models.CharField(
        max_length=200,
        null=False
    )
    last_name = models.CharField(
        max_length=200,
        null=False
    )
    email = models.EmailField(
        max_length=200,
        null=False,
        unique=True
    )
    age = models.PositiveIntegerField(
        null=False
    )
    grade = models.CharField(
        max_length=30,
        null=False
    )
    period = models.CharField(
        max_length=40,
        null=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateField(
        auto_now_add=True
    )