from django.urls import path
from  .views import pedidos



urlpatterns = [
    path("",pedidos,name="pedidos"),
]

