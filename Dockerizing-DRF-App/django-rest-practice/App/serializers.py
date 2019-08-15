from rest_framework import serializers

# models of the App
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer class for serializing the data of Project
    """

    class Meta:
        model = Project
        fields = ("id", "title", "description")

    def update(self, instance, validated_data):
        """
        Update the instance of Project model and return the updated instance
        :param instance: the instance which is going to be update
        :param validated_data: to validate the data of instance
        :return: updated instance of project
        """
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance
