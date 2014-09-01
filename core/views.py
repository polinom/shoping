from rest_framework import generics, permissions, mixins
from .serializers import GroceryItemSerializer, ListItemSerializerGET, ListItemSerializerPOST, ListSerializer
from .models import GroceryItem, ListItem, List


class GroceryItemsList(generics.ListCreateAPIView):
    model = GroceryItem
    serializer_class = GroceryItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = super(GroceryItemsList, self).get_queryset()
        q = self.request.GET.get('q')
        return queryset.filter(title__icontains=q) if q else queryset


class ListsList(generics.ListAPIView, generics.UpdateAPIView):
    model = List
    serializer_class = ListSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = super(ListsList, self).get_queryset()
        a = self.request.GET.get('archived', True)
        return queryset.filter(archived=a)


class ItemsList(generics.ListCreateAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    model = ListItem
    # serializer_class = ListItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = super(ItemsList, self).get_queryset()
        return queryset.filter(root_list__archived=False)

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method in ['POST', 'PUT']:
            return ListItemSerializerPOST
        return ListItemSerializerGET
