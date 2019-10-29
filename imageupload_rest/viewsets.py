from rest_framework import viewsets
from imageupload_rest.serializers import BillImageSerializer
from bill.models import BillImage


class BillImageViewSet(viewsets.ModelViewSet):
    print("BillImageViewSet IN")
    queryset = BillImage.objects.all()
    serializer_class = BillImageSerializer
