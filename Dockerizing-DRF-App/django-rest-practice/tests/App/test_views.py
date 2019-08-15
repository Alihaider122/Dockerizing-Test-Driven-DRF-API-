import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestProjectsList(APITestCase):
    """
    GET projects/
    :test for getting projects instances
    """

    @pytest.mark.django_db
    def test_can_get_project_list(self):
        """
        GET the projects instances
        :return: null
        """
        url = reverse('projects-list-create')
        response = self.client.get(url)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)


class TestProjectCreate(APITestCase):
    """
    POST projects/
    :test for creating projects instance
    """

    @pytest.mark.django_db
    def test_can_post_project(self):
        """
        simple create an instance in the empty database
        :return:
        """
        url = reverse('projects-list-create')
        data = {
            'title': 'test project title',
            'description': 'test project description'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.json()), 3)


class TestSingleProjectDetail(APITestCase):
    """
    GET projects:id/
    :test for getting the single project instance
    """

    @pytest.mark.django_db
    def test_can_get_single_project(self):
        """
        GET the details of single Project instance.
        :return: null
        """
        # get single object
        url = reverse('projects-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 3)


class TestUpdateProjectDetail(APITestCase):
    """
    PUT projects:id/
    :test for updating single project instance
    """

    @pytest.mark.django_db
    def test_can_update_project(self):
        """
        PUT method on single project instance.
        :return: null
        """
        url = reverse('projects-detail', kwargs={'pk': 1})
        data = {
            'title': 'test project title updated',
            'description': 'test project description updated'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], data['title'])
        self.assertEqual(response.json()['description'], data['description'])


class TestDeleteProjectDetail(APITestCase):
    """
    DELETE projects:id/
    :test for deleting single project instance
    """

    @pytest.mark.django_db
    def test_can_update_project(self):
        """
        DELETE method on single project instance.
        :return: null
        """
        url = reverse('projects-detail', kwargs={'pk': 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
