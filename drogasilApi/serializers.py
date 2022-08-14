from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    sku = serializers.CharField()
    name = serializers.CharField()
    image = serializers.CharField()
    thumbnail = serializers.CharField()
    urlKey = serializers.CharField()
    brand = serializers.CharField()
    isInStock = serializers.BooleanField()
    qtyInStock = serializers.IntegerField()
    valueFrom = serializers.FloatField()
    valueTo = serializers.FloatField()
