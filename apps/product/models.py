from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from utils.id_utils import hashid
from apps.account.models import MyUser
import time
# Create your models here.

class Product(models.Model):
    pid = models.CharField(max_length=32,unique=True,editable=False,verbose_name='product_id')
    name = models.CharField(max_length=100,verbose_name='pro_name')
    url = models.URLField(verbose_name='pro_url')
    digest = models.CharField(max_length=200,verbose_name='pro_digst')
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,verbose_name='user')
    vote_count = models.IntegerField(default=0,verbose_name='pro_vote_count')

    public = models.BooleanField(default=True,verbose_name='public')
    remark = models.CharField(max_length=200,default='',blank=True,null=True,
                              verbose_name='decribtion')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product'
        verbose_name = 'products'
        verbose_name_plural = 'pro_manage'

    def __str__(self):
        return '%s(%s)' %(self.name,self.pid)

    def vote(self,user):
        """用户user点赞当前产品"""
        if not ProductVote.voted(user,self):
            pvote = ProductVote()
            pvote.user = user
            pvote.product = self
            pvote.add_time = int(time.time())
            pvote.save()
            self.vote_count += 1
            self.save(update_fields=['vote_count'])




class ProductVote(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    add_time = models.IntegerField(default=0)


    class Meta:
        db_table = 'product_vote'
        verbose_name = 'vote_number'
        verbose_name_plural = 'vote_number_manage'
    @classmethod
    def voted(cls,user,product):
        return cls.objects.filter(user = user,product = product).exists()





@receiver(post_save,sender=Product,dispatch_uid = 'get_product_pid')

def update_uid(sender,instance,**kwargs):
    if not instance.pid:
        instance.pid = hashid(instance.id,length=8) #生成用户uid
        instance.save()
