from django.urls import path
from .views import ListCreateProjectView, ProjectsDetailView

App_name = "App"
urlpatterns = [
    path("projects/", ListCreateProjectView.as_view(), name="projects-list-create"),
    path("projects/<int:pk>/", ProjectsDetailView.as_view(), name="projects-detail")
]
