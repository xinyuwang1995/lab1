from django.test import TestCase
from  .models import Product

class ModelTest(TestCase):
    def setUp(self):
        Product.objects.create(pid='1',name='yandex',url='http://www.yandex.ru',digest='search engine',
                              user_id=1)
        Product.objects.create(pid='2',name='facebook',url='http://www.facebook.com',digest='social',user_id=2)
    def test_product_register(self):
        res = Product.objects.get(name='yandex')
        self.assertEqual(res.url,"http://www.yandex.ru")
    def test_product_gituser_register(self):
        res = Product.objects.get(name='facebook')
        self.assertEqual(res.url,'http://www.facebook.com')
