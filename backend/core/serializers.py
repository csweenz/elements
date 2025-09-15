from rest_framework import serializers
from .models import Element, ElementPrice, PriceSource, Feedstock, FeedstockPrice, ElementFeedstockWeight

class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = ["atomic_number", "symbol", "name"]
        
class PriceSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceSource
        fields = '__all__'

class FeedstockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedstock
        fields = '__all__'

class ElementFeedstockWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementFeedstockWeight
        fields = '__all__'
class ElementPriceSerializer(serializers.ModelSerializer):
    # send/receive atomic_number as the FK field
    element = serializers.PrimaryKeyRelatedField(
        queryset=Element.objects.all(),
        to_field="atomic_number"
    )
    class Meta:
        model = ElementPrice
        fields = ["element", "ts", "price", "currency", "unit", "source"]

class FeedstockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedstockPrice
        fields = '__all__'