from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),        # Página inicial
    path('home/', views.PostView.as_view(), name='home_alt'), # /home/
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
