from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

#물건
class Product(models.Model):
    objects = models.Manager()
    title = models.TextField(max_length=15, null=False) #상품명
    price = models.IntegerField(default=0, null=False) #가격
    info = models.TextField(max_length=200, null=True) #설명
    stock = models.IntegerField(default=0) #재고
    image = models.ImageField(upload_to='images/', null=True) #이미지
    created_at = models.DateTimeField(auto_now_add=True) # 생성시간
    updated_at = models.DateTimeField(auto_now=True) # 수정시간
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_product")

#리뷰
class Review(models.Model):
    objects = models.Manager()
    scores = models.IntegerField(default=0) #평점
    content = models.TextField(max_length=300) #내용
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product") ##상품
    created_at = models.DateTimeField(auto_now_add=True) #생성시간
    updated_at = models.DateTimeField(auto_now=True) #수정시간
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

# Create your models here.
