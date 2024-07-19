from rest_framework import serializers
import os
from deploy.models import RequestEntry
DEPLOYMENT = os.getenv('DEPLOYMENT_STATE=')
from datetime import datetime

class EpochTimeField(serializers.Field):
    def to_representation(self, value):
        return int(value.timestamp())

class RequestEntrySerializerEdit(serializers.ModelSerializer):
        class Meta:
            model = RequestEntry
            fields = ['name', 'created_at']


class RequestEntrySerializerView(serializers.ModelSerializer):
    created_at = EpochTimeField()
    class Meta:
        model = RequestEntry
        fields = ['name','created_at']





