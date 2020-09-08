from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

#물건
class Product(models.Model):
    objects = models.Manager()
    title = models.TextField(max_length=15, null=False) #상품명
    price = models.IntegerField() #가격
    info = models.TextField(max_length=200, null=True) #설명
    stock = models.IntegerField() #재고
    image = models.ImageField(upload_to='images/', null=True) #이미지
    created_at = models.DateTimeField(auto_now_add=True) # 생성시간
    updated_at = models.DateTimeField(auto_now=True) # 수정시간
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_product")

#리뷰
class Review(models.Model):
    objects = models.Manager()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="review") ##상품
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    scores = models.IntegerField(null=True) #평점
    content = models.TextField(max_length=300) #내용
    #related_name은 1:N관계의 모델 Prdocut:Review 관계에서 Product 객체가 Review의 객체들을 불러올때 (Review에 접근할때) 사용
    #따라서 related_name = "review" 가 되면 Product.review.all() 을 통해 호출하는 등의 작업이 가능하다.
    #related_name="product"로 설정한것이 틀리지는 않았지만 의미상으로는 review가 들어가야 한다.
    created_at = models.DateTimeField(auto_now_add=True) #생성시간
    updated_at = models.DateTimeField(auto_now=True) #수정시간
    