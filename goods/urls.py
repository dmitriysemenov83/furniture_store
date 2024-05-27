from django.urls import path
from goods import views
from goods.apps import GoodsConfig

app_name = GoodsConfig.name

urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('<slug:category_slug>/<int:page>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]
