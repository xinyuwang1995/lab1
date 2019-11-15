from django.test import TestCase
from  .models import MyUser,GithubUser

class ModelTest(TestCase):

    def setUp(self):
        MyUser.objects.create(username='test',nickname='test_ac',gender='male',avatar='https://pic1.zhimg.com/v2-fda399250493e674f2152c581490d6eb_1200x500.jpg')
        MyUser.objects.create(nickname='test_gic',gender='female',avatar='https://pic1.zhimg.com/v2-fda399250493e674f2152c581490d6eb_1200x500.jpg')
        GithubUser.objects.create(name='gi_test',email='test@test.com',bio='test_h',user_id=2)
    def test_user_register(self):
        res = MyUser.objects.get(username='test')
        self.assertEqual(res.gender,"male")

    def test_githubuser_register(self):
        res = GithubUser.objects.get(name='gi_test')
        self.assertEqual(res.email,'test@test.com')
