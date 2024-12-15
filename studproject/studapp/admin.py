from django.contrib import admin

from django.contrib import admin
from .models import Student, LibraryHistory, FeesHistory,User


admin.site.register(User)
admin.site.register(Student)
admin.site.register(LibraryHistory)
admin.site.register(FeesHistory)

