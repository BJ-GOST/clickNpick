from django.urls import path 
from. import views 

urlpatterns = [
    path('post-product', views.post_product, name='post-product'),
    path('products', views.products, name='products'),
    path('product-detail/<str:pk>/', views.product_detail, name='product-detail'),
    path('update-product/<str:pk>/', views.update_product, name='update-product'),
    path('delete-product/<str:pk>/', views.delete_product, name='delete-product')
    
]