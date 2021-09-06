from rest_framework import serializers
from ..models import Category, Notebook, Customer, Order


class CategorySerializers(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class BaseProductSerializer:
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)
    title = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    image = serializers.ImageField(required=False)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=9, decimal_places=2, required=True)


class NotebookSerializer(BaseProductSerializer, serializers.ModelSerializer):
    diagonal = serializers.CharField(required=True)
    display_type = serializers.CharField(required=True)
    processor_freq = serializers.CharField(required=True)
    ram = serializers.CharField(required=True)
    video = serializers.CharField(required=True)
    time_without_charge = serializers.CharField(required=True)

    class Meta:
        model = Notebook
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True)

    class Meta:
        model = Customer
        fields = '__all__'

