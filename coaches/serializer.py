from rest_framework import serializers
from .models import TrenerModel


class TrenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrenerModel
        fields = ('first_name', 'last_name', 'date_of_birth', 'image', 'user')
