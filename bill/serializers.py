from django.contrib.auth.models import User
from rest_framework import serializers
from bill.models import Bill


class BillSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bill
        fields = ('id', 'owner', 'created', 'billDate', 'amount', 'title', 'description', 'image')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    bills = serializers.HyperlinkedRelatedField(many=True, view_name='bill-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'bills')

