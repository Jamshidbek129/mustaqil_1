from .views import Yaratish, Foydalanuvchi,Ochir
from django.urls import path

urlpatterns=[
    path("", Yaratish.as_view(), name="olma"),
    path("j/", Foydalanuvchi.as_view(), name="uzum"),
    path("<int:pk>/delete/", Ochir.as_view(), name="del"),
]
