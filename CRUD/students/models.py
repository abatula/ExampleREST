from django.db import models

class Student(models.Model):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])

    def GetFullName(self):
        return ' '.join([self.first_name, self.last_name])
