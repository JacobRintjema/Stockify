from django.contrib import admin
from django.urls import path
from stockApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('active_stocks/', views.activeS, name='active-stocks'),
    path('idk.html', views.idk, name='idk'),
    path('historical.csv', views.historical, name='lol'),
    path('stock/<int:stock_id>/', views.stock_detail, name='stock_detail')
]
