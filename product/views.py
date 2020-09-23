from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Review, Like
from django.contrib.auth.decorators import login_required


def new(req):
    return render(req, 'product/new.html')

def create(request):
    if request.method == 'POST':
        product_seller = request.user
        product_title = request.POST.get('title')
        product_stock = request.POST.get('stock')
        product_price = request.POST.get('price')
        product_info = request.POST.get('info')
        product_image = request.FILES.get('image')
        Product.objects.create(title=product_title, price=product_price, image=product_image,  info=product_info, seller=product_seller, stock=product_stock)
    return redirect('product:main_list')

def main_list(request):
    products = Product.objects.all().order_by("-created_at")
    #Product의 객체들을 products라는 이름으로저장
    return render(request, 'product/main_list.html', {'products': products })
    #return하며 main_list를 렌더링하는데, products객체들을 products라는 이름의 딕셔너리에 추가해서 보낸다.

def show(request, id):
    product = Product.objects.get(pk=id)
    product.view_count += 1
    product.save()
    all_reivew = product.review.all().order_by('-created_at')
    return render(request, 'product/show.html', {'product': product, 'review':all_reivew })

def update(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        product.title = request.POST.get('title')
        product.stock = request.POST.get('stock')
        product.price = request.POST.get('price')
        product.image = request.FILES.get('image')
        product.info = request.POST.get('info')
        product.save()
        return redirect('product:show', product.id)
    return render(request, 'product/update.html', {'product': product})
        
def delete(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('product:main_list')

def post_like(request, id):
    product = get_object_or_404(Product, pk=id)
    #좋아요 취소
    if request.user in product.like_user_set.all():
        product.like_user_set.remove(request.user)
    else:
        product.like_user_set.add(request.user)

    if request.GET.get('redirect_to') == 'show':
        return redirect('product:show', id)
    else:
        return redirect('product:main_list')

def create_review(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        writer = request.user
        review_scores = request.POST.get('scores') #html에서 scores라는 form을 찾고, 그 input값을 가져와서 모델링 해두었던 scores변수에 담는다.
        review_content = request.POST.get('content')
        Review.objects.create(content=review_content, product=product, reviewer=writer, scores=review_scores)
    return redirect('product:show', product_id)

def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    product_id = review.product.id
    review.delete()
    return redirect('product:show', product_id)
    #return 부분이랑 html넘어가는 부분이 뭔가 틀렸는데 잘 모르게쓰여ㅠㅠ

    #그리고 update는 잘 모르겠습니다ㅠㅠ

def update_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        product_id = review.product.id
        review.content = request.POST.get('content')
        review.scores = request.POST.get('scores')
        review.save()
        return redirect('product:show', product_id)
    return render(request, 'product/update_review.html', {'review' : review})

#좋아요 한 상품 목록을 보여주는건 조금 더 생각을 해볼게여!

@login_required
def like_list(request):
    likes = Like.objects.filter(user=request.user)
    ## 또는 likes = request.user.like_set.all()
    return render(request, 'product/like_list.html', {'likes':likes})
