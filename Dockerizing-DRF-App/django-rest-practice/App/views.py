from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from .decoraters import validate_request_data

from .models import Project
from .serializers import ProjectSerializer


# Create your views here.
class ListCreateProjectView(generics.ListCreateAPIView):
    """
    GET projects/
    POST projects/
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @validate_request_data
    def post(self, request, *args, **kwargs):
        a_project = Project.objects.create(
            title=request.data["title"],
            description=request.data["description"]
        )
        return Response(
            data=ProjectSerializer(a_project).data,
            status=status.HTTP_201_CREATED
        )


class ProjectsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET projects/:id/
    PUT projects/:id/
    DELETE projects/:id/
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_song = self.queryset.get(pk=kwargs["pk"])
            return Response(ProjectSerializer(a_song).data)
        except Project.DoesNotExist:
            return Response(
                data={
                    "message": "Project with id: {0} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            a_song = self.queryset.get(pk=kwargs["pk"])
            serializer = ProjectSerializer()
            updated_project = serializer.update(a_song, request.data)
            return Response(ProjectSerializer(updated_project).data)
        except Project.DoesNotExist:
            return Response(
                data={
                    "message": "Project with id: {0} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            a_song = self.queryset.get(pk=kwargs["pk"])
            a_song.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            return Response(
                data={
                    "message": "Project with id: {0} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
