from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
app_name = 'app1'
urlpatterns = [
    path('',views.create_user , name='signup'),
    path('login/', views.login_user , name='login'),
    path('home/' , views.home , name='home'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('setting/' , views.setting_view , name='setting'),
    path('ajax/general/',views.general,name='general'),
    path('usersentdata/',views.usersentdata , name='usersentdata'),
    path('passvalidation/',views.passwordvalidation,name='passvalidation'),
    path('addtocart/',views.addtocart,name='addtocart'),
    path('cart/' , views.cartshow,name='cart'),
    path('qntcng/',views.qntcng , name='qntcng'),
    path('bigview/<int:id>/',views.bigpicview ,name='bigview'),
    path('profilepic/', views.imagechange , name='porfilepic'),
]
