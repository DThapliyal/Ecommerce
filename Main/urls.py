from django.urls import path
from Main import views   #import views from ProjectApp.

urlpatterns = [
    path('',views.Ecommercefun,name='Ecommerce'),
    path('del/<int:id>/',views.delete_Product,name='delete'),#we have used dynamic URL here, which will store data at the time of request.
    path('edit/<int:id>/',views.update_Product,name='edit'),
    path('api',views.ecommerce_api),
]

'''Also we have created a urls.py file here in Project app
so the code look clean and we will link this folder 
to the Actual urls.py folder through include Function.'''