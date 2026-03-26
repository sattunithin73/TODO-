from django.urls import path
from .views import * 

urlpatterns = [
    path('',home,name='home'),
    path('add/',add,name='add'),
    path('complete/',complete,name='complete'),
    path('trash/',trash,name='trash'),
    path('about/',about,name='about'),
    path('complete_h/<int:id>',complete_h,name='complete_h'),
    path('complete_allh/',complete_allh,name='complete_allh'),
    path('delete_h/<int:id>',delete_h,name='delete_h')
]