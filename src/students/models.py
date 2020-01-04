from datetime import datetime

from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    email = models.EmailField()
    telephone = models.CharField(max_length=16)
    address = models.CharField(max_length=255, null=True)

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.birth_date}'


    @classmethod
    def generate_student(cls):
        student = cls(
            first_name='vadim',
            last_name='krav',
            birth_date=datetime.now().date(),
            email='fdgsgggsg@gmail.com',
            telephone='525554535'
        )
        student.save()
