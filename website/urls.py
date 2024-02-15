from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),    
#path('login/', views.login_user, name='login'),
path('logout/', views.logout_user, name='logout'),
path('register/', views.register_user, name='register'),
#http://127.0.0.1:8000/record/1 same as localhost/8000/record/1
path('record/<int:pk>', views.show_record, name='record'),
path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
path('add_record/', views.add_record, name='add_record'),
path('update_record/<int:pk>', views.update_record, name='update_record'),

]
