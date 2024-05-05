from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User

class MyTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='tutor',
            password='tutor123'
        )
        self.client.login(username='tutor', password='tutor123')

    def test_my_endpoint(self):
        url = reverse('create-post')
        data = {"question": "test_ques",
                "answer": "test_ans",
                "category": "test_cate",
                "topic": "test_topic",
                "student_name": "test_std_name",
                "company": '',
                "links": "test_link"}
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, 200)


# from django.test import TestCase
# from django.urls import reverse
# from rest_framework.test import APITestCase
# from rest_framework import status
# # from .views import CreatePost

# # Create your tests here.

# class MyTestCase(APITestCase):
#     def test_create_object(self):
#         url = reverse('create-post')
#         data = {"question": "test_ques",
#                 "answer": "test_ans",
#                 "category": "test_cate",
#                 "topic": "test_topic",
#                 "student_name": "test_std_name",
#                 "company": '',
#                 "links": "test_link"}
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data['question'], 'test_ques')

# from django.urls import reverse
# from rest_framework.test import APITestCase, APIClient
# import base64
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User

# class MyTest(APITestCase):
#     def setUp(self):
#         self.client = APIClient()
#         url = reverse('create-post')
#         username = 'tutor'
#         password = 'tutor123'
#         self.credentials = base64.b64encode(f'{username}:{password}'.encode()).decode()
#         self.response = self.client.get(url, HTTP_AUTHORIZATION=f'Basic {self.credentials}')
#         # response = client.get('/example/', HTTP_AUTHORIZATION=f'Basic {credentials}')
#         # self.user = User.objects.create_user(
#         #     username='tutor',
#         #     password='tutor123'
#         # )
#         # self.token = Token.objects.create(user=self.user)
#         # self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


#     def test_my_endpoint(self):
#         url = reverse('create-post')
#         data = {"question": "test_ques",
#                 "answer": "test_ans",
#                 "category": "test_cate",
#                 "topic": "test_topic",
#                 "student_name": "test_std_name",
#                 "company": '',
#                 "links": "test_link"}
#         # response = self.client.post(url,data,format='json',HTTP_AUTHORIZATION=f'Basic {self.credentials}')
#         # client.get('/example/', HTTP_AUTHORIZATION=f'Basic {self.credentials}')
#         self.assertEqual(self.response.status_code, 200)
#         # self.assertEqual(self.response.data['question'], 'test_ques')