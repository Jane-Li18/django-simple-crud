from django.contrib import admin  
from django.urls import path  
from souvenirs import views  

urlpatterns = [  
    path('', views.reg),  
    path('reg', views.reg),  
    path('records',views.records),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  