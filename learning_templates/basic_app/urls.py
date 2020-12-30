from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
                    path('', views.index, name = 'home_page'),
                    path('relative/', views.relative, name = 'relative_page'),
                    path('other/', views.other, name = 'other_pages'),
              ]
