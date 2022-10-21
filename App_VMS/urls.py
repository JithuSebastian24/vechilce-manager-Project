from django import views
from django.urls import path
from App_VMS import views
app_name='App'

urlpatterns = [
     path('',views.index,name='index'),
     path('superadminlogin/',views.superadminlogin,name='superadminlogin'),
     path('adminlogin/',views.adminlogin,name='adminlogin'),
     path('userlogin/',views.userlogin,name='userlogin'),
     path('registration/',views.registration,name='registration'),
     path('DetailUserview/<int:id>',views.DetailUserview,name='DetailUserview'),
     path('edit/<int:id>',views.edit,name='edit'),
     path('update/',views.update,name='update'),
     path('delete/<int:id>',views.delete,name='delete'),

]