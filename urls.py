from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('userhome/', views.user_home, name='userhome'),
    path('adminhome/', views.admin_home, name='adminhome'),
    path('unknownhome/', views.unknown_home, name='unknownhome'),
    path('addproduct/', views.add_product, name='addproduct'),
    path('editproduct/<int:id>', views.update_product, name='editproduct'),
    path('deleteproduct/<int:id>', views.delete_product, name='deleteproduct'),
]
