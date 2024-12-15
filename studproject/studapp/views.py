from django.shortcuts import render
from rest_framework import permissions
from rest_framework import status
from .models import Student, LibraryHistory, FeesHistory
from .serializers import StudentSerializer, LibraryHistorySerializer, FeesHistorySerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Token View to obtain the token
from rest_framework.authtoken.views import obtain_auth_token


# Custom Token View for Login
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = User.objects.filter(username=username).first()
        
        if user is not None and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid credentials"}, status=400)

from rest_framework import permissions

class RoleBasedPermission(permissions.BasePermission):
    allowed_roles = []

    def has_permission(self, request, view):
        user_role = getattr(request.user, 'role', None)  
        return user_role in self.allowed_roles if user_role else False

class IsAdminOfficeStaffLibrarian(RoleBasedPermission):
    allowed_roles = ['Admin', 'office_staff', 'librarian']



class AdminDashboard(APIView):

    def get(self, request):
        students = Student.objects.all()
        students_serializer = StudentSerializer(students, many=True)
        return Response(students_serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OfficeStaffDashboard(APIView):

    def get(self, request):
        students = Student.objects.all()
        students_serializer = StudentSerializer(students, many=True)
        return Response(students_serializer.data)

class LibrarianDashboard(APIView):

    def get(self, request):
        library_history = LibraryHistory.objects.all()
        library_serializer = LibraryHistorySerializer(library_history, many=True)
        return Response(library_serializer.data)

