from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


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
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data, 
            status=status.HTTP_201_CREATED
        ) 

    # /api/students/<str:id>
    def retrieve(self, request, pk=None):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    
    # /api/students/<str:id>
    def update(self, request, pk=None):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(
            instance=student,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data, 
            status=status.HTTP_202_ACCEPTED
        ) 


    # /api/students/<str:id>
    def remove(self, request, pk=None):
        student = Student.objects.get(id=pk)
        student.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )




    