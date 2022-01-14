from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)


    class Meta:
        model = News
        fields = ['id', 'title', 'body', 'created_at', 'updated_at']
