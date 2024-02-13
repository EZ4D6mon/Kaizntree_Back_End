from rest_framework import serializers
from .models import Item, Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    category_detail = serializers.SerializerMethodField(read_only=True)
    tags_detail = serializers.SerializerMethodField(read_only=True)

    # For write operations
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, write_only=True)

    class Meta:
        model = Item
        fields = ['id', 'sku', 'name', 'category', 'tags', 'category_detail', 'tags_detail', 'stock_status', 'available_stock', 'created_at']

    def get_category_detail(self, obj):
        return CategorySerializer(obj.category).data

    def get_tags_detail(self, obj):
        return TagSerializer(obj.tags.all(), many=True).data