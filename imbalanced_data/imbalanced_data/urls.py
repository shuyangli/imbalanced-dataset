from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from data_app import views
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
#router.register(r'datasets', views.DatasetViewSet)
#router.register(r'classifiers', views.ClassifierViewSet)
# urlpatterns = [
#     url(r'^$', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     url(r'^admin/', include(admin.site.urls)),
# ]

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/groups/$', csrf_exempt(views.GroupList.as_view())),
    url(r'^api/analyses/$', csrf_exempt(views.AnalysisTaskList.as_view())),
    url(r'^api/users/$', csrf_exempt(views.UserList.as_view())),
    url(r'^api/test_outputs/$', csrf_exempt(views.TestOutputList.as_view())),
    url(r'^api/datasets/$', csrf_exempt(views.DatasetList.as_view())),
    url(r'^api/datasets/(?P<pk>[0-9]+)/$', views.DatasetDetail.as_view()),
    url(r'^api/classifiers/$', csrf_exempt(views.ClassifierList.as_view())),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
