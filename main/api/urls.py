from django.urls import include, path, re_path
from rest_framework import routers
from .views import UniViewSet, DegViewSet, getMetadata, MdataViewSet
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r"universities", UniViewSet)
router.register(r"degrees", DegViewSet)
router.register(r"mdata", MdataViewSet)


urlpatterns = [
    path("", include(router.urls)),
    re_path(r"mdata/tokenid/(?P<pk>[0-9]+)$", getMetadata),
]
