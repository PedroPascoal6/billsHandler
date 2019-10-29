from django.conf.urls import url, include
from rest_framework import routers
from imageupload_rest.viewsets import BillImageViewSet
# from imageupload_rest.forms import UploadFileForm

router = routers.DefaultRouter()
# router.register('images', BillImageViewSet, 'images')

urlpatterns = [
    url(r'^', include(router.urls))
]
