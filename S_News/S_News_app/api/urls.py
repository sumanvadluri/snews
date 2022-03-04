from django.urls import path,include
from django.contrib import admin
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from S_News_app.api import views

from rest_framework.routers import DefaultRouter

# router=DefaultRouter()
# router.register(r'devices', FCMDeviceAuthorizedViewSet)

urlpatterns=[
    # path('^',include(router.urls)),
    path('news',views.News_view.as_view()),
    path('category',views.News_Category.as_view()),
    path('full_image',views.Full_image.as_view()),

    # path('filter',views.News_get.as_view()),


    # path(r'^viewset2/$', 'News_view', name='demo2'),
    # path('viewset',views.viewset.as_view()),

    # path(r'^devices?$', FCMDeviceAuthorizedViewSet.as_view({'post': 'create'}),name='create_fcm_device'),




]