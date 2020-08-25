from django.urls import path
from .views import *

app_name = "product"

urlpatterns = [
    path('new/', new, name="new"),
    path('main_list/', main_list, name="main_list"),
    path('create/', create, name="create"),
    path('show/<int:id>', show, name="show"),
    path('update/<int:id>', update, name="update"),
    path('deltete/<int:id>', delete, name="delete"),
    path('like/<int:id>', like, name="like"),
    path('create_review/<int:product_id>', create_review, name="create_review"),
    path('delete_review/<int:review_id>', delete_review, name="delete_review"),
]