from django.urls import path
from users import views
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]
