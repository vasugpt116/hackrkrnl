from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    detail = models.TextField()
    tasks1 = [
        ('Pending', 'Pending'),
        ('Done', 'Done'),
    ]
    status = models.CharField(max_length=7, choices=tasks1)
    def __str__(self):
        return f'{self.detail} - {self.get_status_display()}'