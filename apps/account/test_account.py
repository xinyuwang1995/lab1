from django.test import TestCase
from  .models import MyUser,GithubUser

class ModelTest(TestCase):

    def setUp(self):
        MyUser.objects.create(username='test',nickname='test_ac',gender='male',avatar='https://pic1.zhimg.com/v2-fda399250493e674f2152c581490d6eb_1200x500.jpg')

    def test_user_register(self):
        res = MyUser.objects.get(username='test')
        self.assertEqual(res.gender,"male")
