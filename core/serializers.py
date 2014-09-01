from rest_framework import serializers, response, status
from .models import GroceryItem, List, ListItem


class GroceryItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroceryItem
        fields = ('id', 'title', 'price', 'unit', 'favorit',)


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('id', 'crated', 'archived')


# serializer for GET method
class ListItemSerializerGET(serializers.ModelSerializer):

    # grocery = GroceryItemSerializer()
    grocery = GroceryItemSerializer()
    root_list = serializers.PrimaryKeyRelatedField(source='root_list')

    class Meta:
        model = ListItem
        fields = ('id', 'grocery', 'purchased', 'items', 'root_list')


class ListItemSerializerPOST(serializers.ModelSerializer):

    # grocery = GroceryItemSerializer()
    grocery = serializers.PrimaryKeyRelatedField(source='grocery')
    root_list = serializers.PrimaryKeyRelatedField(source='root_list')

    class Meta:
        model = ListItem
        fields = ('id', 'grocery', 'items', 'purchased', 'root_list')
