from django.urls import path
from .views import home_view, dashboard, basic_view, intermediate_view, advanced_view

urlpatterns = [
    path('', home_view, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('basic/', basic_view, name='basic_view'),
    path('intermediate/', intermediate_view, name='inter_view'),
    path('advanced/', advanced_view, name='advance_view'),
]
