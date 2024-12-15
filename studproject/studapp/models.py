from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission


from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User



class User(AbstractUser):
    role = models.CharField(max_length=50, null=True,choices=[('Admin','Admin'), ('office_staff','Office Staff'), ('librarian', 'Librarian')])


    groups = models.ManyToManyField(
    Group,
        related_name='custom_user_set',  # Change the reverse relationship name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Change the reverse relationship name
        blank=True
    )
    

from django.contrib.auth import get_user_model



class Student(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)    
    name = models.CharField(max_length=255,default='Default Name')
    roll_number = models.CharField(max_length=20, unique=True,default='Default Name')
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=50,default='Default Name')
    dob = models.DateField()

    def __str__(self):
        return self.name

class LibraryHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=255)
    borrow_date = models.DateField()
    return_date = models.DateField()
    status = models.CharField(max_length=50)  # e.g., borrowed, returned

    def __str__(self):
        return f"{self.book_name} borrowed by {self.student.name}"

class FeesHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    remarks = models.TextField()

    def __str__(self):
        return f"{self.fee_type} for {self.student.name}"
