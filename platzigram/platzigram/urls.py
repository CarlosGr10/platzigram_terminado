"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(('post.urls', 'post'), namespace='posts')),
    
    path('user/', include(('user.urls', 'user'), namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Antes

# from platzigram import views as local_views
# from post import views as app_views
# from user import views as user_views

    # path('admin/', admin.site.urls),
    # path('local/',local_views.lis),
    # path('app/',app_views.lista, name = 'app'),
    # path('posts/news',app_views.create_post,name = 'crete_post'),
    # path('user/login',user_views.login_view, name = 'login'),
    # path('user/logout', user_views.logout_view, name = 'logout'),
    # path('user/signup',user_views.signup, name = 'signup'),
    # path('user/me/profile',user_views.update_profile, name = 'update_profile')