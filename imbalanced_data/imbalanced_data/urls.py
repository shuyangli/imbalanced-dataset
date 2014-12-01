from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from data_app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'datasets', views.DatasetViewSet)
router.register(r'classifiers', views.ClassifierViewSet)
# urlpatterns = [
#     url(r'^$', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     url(r'^admin/', include(admin.site.urls)),
# ]

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),

]
