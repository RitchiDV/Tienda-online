from django.urls import path
from  .views import VRegistro,log_out,logear



urlpatterns = [
    path("",VRegistro.as_view(),name="login"),
    path("logout",log_out,name="logout"),
    path("logear",logear,name="logear"),
    
]

