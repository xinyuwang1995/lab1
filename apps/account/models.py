from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.account.const import GENDERS,GENDER_N
from utils.id_utils import hashid
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class MyUser(AbstractUser):
    uid = models.CharField(max_length=32,unique=True,editable=False,verbose_name='user_id')
    nickname = models.CharField(max_length=50,blank=True,null=True,
                                default='',verbose_name='nickname')
    gender = models.CharField(max_length=10,choices=GENDERS,
                              default=GENDER_N,verbose_name='gender')
    avatar = models.CharField(max_length=500,default='',verbose_name='head_portrait')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'myuser'
        verbose_name = 'users'
        verbose_name_plural = 'user_manage'

    def __str__(self):
        return self.username


@receiver(post_save,sender=MyUser,dispatch_uid = 'get_myuser_uid')

def update_uid(sender,instance,**kwargs):
    if not instance.uid:
        instance.uid = hashid(instance.id) #生成用户uid
        instance.save()

class GithubUser(models.Model):
    gid = models.CharField(max_length=50,editable=False)
    user = models.ForeignKey(MyUser,blank=True,null=True,on_delete=models.CASCADE )

    login = models.CharField(max_length=100)
    name = models.CharField(max_length=200,blank=True,null=True,default='')
    email = models.CharField(max_length=100,blank=True,null=True,default='')
    bio = models.CharField(max_length=200,blank=True,null=True,default='')
    location = models.CharField(max_length=200,blank=True,null=True,default='')
    repos_url = models.URLField()

    avatar_url = models.URLField()
    url = models.URLField()
    followers_url = models.URLField()
    subscriptions_url = models.URLField()

    html_url = models.URLField()
    organizations_url = models.URLField()
    public_gists = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    public_repos = models.IntegerField(default=0)
    created_at = models.CharField(max_length=20)
    updated_at = models.CharField(max_length=20)

    class Meta:
        db_table = 'github_user'
        verbose_name = 'Githubuser'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.login


"""
{
  "login": "octocat",
  "id": 1,
  "node_id": "MDQ6VXNlcjE=",
  "avatar_url": "https://github.com/images/error/octocat_happy.gif",
  "gravatar_id": "",
  "url": "https://api.github.com/users/octocat",
  "html_url": "https://github.com/octocat",
  "followers_url": "https://api.github.com/users/octocat/followers",
  "following_url": "https://api.github.com/users/octocat/following{/other_user}",
  "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
  "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
  "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
  "organizations_url": "https://api.github.com/users/octocat/orgs",
  "repos_url": "https://api.github.com/users/octocat/repos",
  "events_url": "https://api.github.com/users/octocat/events{/privacy}",
  "received_events_url": "https://api.github.com/users/octocat/received_events",
  "type": "User",
  "site_admin": false,
  "name": "monalisa octocat",
  "company": "GitHub",
  "blog": "https://github.com/blog",
  "location": "San Francisco",
  "email": "octocat@github.com",
  "hireable": false,
  "bio": "There once was...",
  "public_repos": 2,
  "public_gists": 1,
  "followers": 20,
  "following": 0,
  "created_at": "2008-01-14T04:33:35Z",
  "updated_at": "2008-01-14T04:33:35Z"
}
"""