from django.shortcuts import render
from apps.product.form import ProductForm
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseForbidden,JsonResponse
from django.urls import reverse
from apps.product.models import Product
# Create your views here.
def new_product_view(request):
    if request.user.is_authenticated:
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('index'))
        return HttpResponse('<h1>product share error~~~</h1>')
    else:
        return HttpResponseForbidden('<h1>not login~~</h1>')

def vote_product_view(request):
    pid = request.POST.get('pid',None)
    if pid is None:
        return JsonResponse({'errcode':400,'message':'parameter error'})
    if request.user is None or not request.user.is_authenticated:
        return JsonResponse({'errcode':401,'message':'not login'})



    try:
        product = Product.objects.get(pid = pid)
        product.vote(request.user)
        return  JsonResponse({'errcode':200,'message':'success','data':{
            'vote_count':product.vote_count
        }})
    except Product.DoesNotExist:
        return JsonResponse({'errcode':404 ,'message':'product not exist'})


    pass