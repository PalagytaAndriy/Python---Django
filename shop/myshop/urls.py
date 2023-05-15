from django.urls import path
from . import views

app_name = 'myshop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('shop', views.product_list, name='product_list'),

    path('about_us', views.about_us, name='about_us'),
    path('shop', views.shop, name='shop'),
    path('zamovnuku', views.zamovnuku, name='zamovnuku'),
    path('hero', views.hero, name='hero'),
    path('zakaz', views.zakaz, name='zakaz'),
    path('order_l', views.order_l, name='order_l'),

    path('portfolio', views.portfolio_list, name='portfolio_list'),

    path('<slug:category_slug>', views.product_list, name='product_list_by_category'),

    path('<int:id>/<slug:slug>', views.product_detail, name='product_detail'),


]
