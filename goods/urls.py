from django.urls import path
from goods import views
from goods.apps import GoodsConfig

app_name = GoodsConfig.name

urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]
