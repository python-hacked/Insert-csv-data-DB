
from django.urls import path
from .views import insert_data,stock_list

urlpatterns = [
    path('insert/', insert_data, name='insert_data'),
    path('stocks/', stock_list, name='stock_list'),

]
