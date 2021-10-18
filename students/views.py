from rest_framework import viewsets
from rest_framework.response import Response
from .models import Student
from serializers import StudentSerializer

class StudentViewSet(viewsets.ViewSet):
    
    # /api/students
    def list(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(
            students,
            many=True
        )
        return Response(serializer.data)

    # /api/students
    def create(self, request):
        pass 


    # /api/students/<str:id>
    def retrieve(self, request, pk=None):
        pass
    
    
    # /api/students/<str:id>
    def update(self, request, pk=None):
        pass


    # /api/students/<str:id>
    def remove(self, request, pk=None):
        pass




    