from todoapp import views
from django.urls import path, include

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/',views.update,name='update'),
]
