from django.urls import path
from goods import views
from goods.apps import GoodsConfig

app_name = GoodsConfig.name

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product'),
]
