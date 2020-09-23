from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

#물건
class Product(models.Model):
    objects = models.Manager()
    title = models.TextField(max_length=15, null=False) #상품명
    info = models.TextField(max_length=200, null=True) #설명
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.IntegerField() #가격
    stock = models.IntegerField() #재고
    view_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True) #이미지
    created_at = models.DateTimeField(auto_now_add=True) # 생성시간
    updated_at = models.DateTimeField(auto_now=True) # 수정시간
    like_user_set = models.ManyToManyField(User, blank=True, related_name="like_user_set", through="Like")

    @property
    def like_count(self):
        return self.like_user_set.count()

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
    
class Like(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together =(('user','product')) #함께 유일해야하는 필드의 쌍을 의미한다. Like모델에서 user와 product의 쌍은 고유하다.
    #메타데이터를 추가하기위한 모델 내부 클래스
    #모델 단위에서 설정할 수 있는 옵션    