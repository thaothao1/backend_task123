from django.urls import path , include
from knox import views as knox_views
from .views import Register , LoginView , RegisterToken , LoginToken
urlpatterns = [
    path('register/' , Register.as_view()),
    path('login/' , LoginView.as_view()),
    path('register_token/' , RegisterToken.as_view()),
    path('login_token/' , LoginToken.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name='logout')


] 