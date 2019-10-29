from rest_framework import serializers
from bill.models import BillImage


class BillImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillImage
        fields = ('pk', 'created', 'owner', 'image',)
