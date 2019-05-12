from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path("professores/", views.professores, name='professores')
]