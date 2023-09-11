from rest_framework import serializers
from .models import New


class NewSerializers(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('title', 'image', 'text', 'created_at', 'user')