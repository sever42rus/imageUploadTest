from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ('id', 'img_url', )

    def get_img_url(self, instance):
        return instance.img.url


class ImageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'img',)
