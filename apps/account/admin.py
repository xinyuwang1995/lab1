from django.contrib import admin
from apps.account.models import MyUser,GithubUser
from apps.product.models import Product
from django.utils.safestring import mark_safe
# Register your models here.

class ProductInline(admin.TabularInline):
    model = Product


class MyUserAdmin(admin.ModelAdmin):
    def avatar_view(self,obj):
        html_tag = "<div><img src='%s></div>'"%obj.avatar
        return mark_safe(html_tag)


    inlines = [ProductInline] #内联产品管理
    list_display = ('uid','username','nickname','avatar_view','is_active','is_staff')



admin.site.register(MyUser,MyUserAdmin)
admin.site.register(GithubUser)
