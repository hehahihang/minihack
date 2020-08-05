from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

class Product(models.Model):
    title = models.TextField(max_length=20, null=False) #상품명
    info = models.TextField(max_length=200) #설명
    price = models.IntegerField(default=0, null=False) #가격
    stock = models.IntegerField() #재고
    image = models.ImageField(upload_to='images/', null=True) #이미지
    created_at = models.DateTimeField(auto_now_add=True) # 생성시간
    updated_at = models.DateTimeField(auto_now=True) # 수정시간
    user = models.ForeignKey(User, on_delete=models.CASCADE) ##판매자

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) ##작성자
    scores = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(100)]) #평점
    content = models.TextField(max_length=300) #내용
    product = models.ForeignKey(Product, on_delete=models.CASCADE) ##상품
    created_at = models.DateTimeField(auto_now_add=True) #생성시간
    updated_at = models.DateTimeField(auto_now=True) #수정시간

# Create your models here.
