
from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import MyProfileApi

app_name = 'appBackend'

# myProfileApi_display = MyProfileApi.as_view({
#     'get': 'list',
# })
# myProfileApi_change = MyProfileApi.as_view({
#     'put': 'update'
# })

router = DefaultRouter()
router.register(r'myProfile', MyProfileApi)

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('menu/', views.MenuView.as_view(),name='menu'),
    path('api/', include(router.urls))
]
