"""Daily_news_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from S_News_app import views


urlpatterns = [
    path('snews/admin/', admin.site.urls),
    path('snews/', views.index_view,name='index'),
    path('snews/home', views.Home_view,name='home'),
    path('snews/create', views.Create_view,name='Create_view'),
    path('snews/login', views.login_view,name='login'),
    path('snews/logout', views.logout,name='logout'),
    path('snews/admin_home', views.admin_home,name='adminhome'),
    path('snews/discrption/<int:id>/', views.discription,name='Discrption_news'),
    path('snews/discrption_user/<int:id>/', views.discription_user_news,name='Discrption_user_news'),
    path('snews/Update_news/<int:id>/', views.News_update,name='updatenews'),
    path('snews/deletenews/<int:id>/', views.News_delete,name='Deletenews'),
    path('snews/update_save/<int:id>/', views.update_save,name='update_data'),
    path('snews/viewset/',include('S_News_app.api.urls')),
    path('snews/fullimage_create',views.Full_Image_Video_view,name='full_image_video'),
    path('snews/full_image_home',views.image_video_home,name='image_video_home'),
    path('snews/full_image_Discription/<int:id>/',views.image_video_view,name='image_video_view'),
    path('snews/full_image_video_update/<int:id>/',views.image_video_update,name='image_video_update'),
    path('snews/full_image_video_update_save/<int:id>/',views.image_video_update_save,name='image_video_updatesave'),
    path('snews/full_image_delete/<int:id>/',views.Full_image_delete,name='full_image_delete'),
    path('snews/Universal_home_page',views.Universal_home,name='Universal_home'),
    path('snews/English_home_page',views.English_home,name='English_home'),








    # path('jsondata',views.json_view),
]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)