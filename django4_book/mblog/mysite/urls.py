from django.urls import path

from mysite import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('post/<slug:slug>/', views.show_post, name='show_post'),
]
