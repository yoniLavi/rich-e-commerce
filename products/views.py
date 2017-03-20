from django.shortcuts import render
from models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})







class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
