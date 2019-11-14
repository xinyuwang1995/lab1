from django.test import TestCase
from  .models import Product

class ModelTest(TestCase):
    def setUp(self):
       Product.objects.create(pid='1',name='yandex',url='http://www.yandex.ru',digest='search engine',
                              user_id=1)


    def test_product_register(self):
        res = Product.objects.get(name='yandex')
        self.assertEqual(res.url,"http://www.yandex.ru")