from rest_framework.viewsets import ModelViewSet

from .serializers import ProductTypeSerializer, HeatLevelSerializer, ProductSerializer,\
    ProductPriceSerializer, OrderDetailSerializer, SweetLevelSerializer, OrderSerializer,\
    MemberSerializer, SessionStatusSerializer, SessionSerializer, OrderDetailTypeSerializer, \
    PointSerializer, PromotionSerializer, ViewProductPriceSerializer

from .models import ProductType, HeatLevel, Product, ProductPrice, OrderDetail,  \
     SweetLevel, Order, Member, SessionStatus, Session, Point, Promotion, OrderDetailType

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

class ViewProductPriceViewSet(ModelViewSet):
    queryset = ProductPrice.objects.order_by('pk')
    serializer_class = ViewProductPriceSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['product',]

class ProductTypeViewSet(ModelViewSet):
    queryset = ProductType.objects.order_by('pk')
    serializer_class = ProductTypeSerializer


class HeatLevelViewSet(ModelViewSet):
    queryset = HeatLevel.objects.order_by('pk')
    serializer_class = HeatLevelSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.order_by('pk')
    serializer_class = ProductSerializer


class ProductPriceViewSet(ModelViewSet):
    queryset = ProductPrice.objects.order_by('pk')
    serializer_class = ProductPriceSerializer


class OrderDetailTypeViewSet(ModelViewSet):
    queryset = OrderDetailType.objects.order_by('pk')
    serializer_class = OrderDetailTypeSerializer



class OrderDetailViewSet(ModelViewSet):
    queryset = OrderDetail.objects.order_by('pk')
    serializer_class = OrderDetailSerializer



class SweetLevelViewSet(ModelViewSet):
    queryset = SweetLevel.objects.order_by('pk')
    serializer_class = SweetLevelSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.order_by('pk')
    serializer_class = OrderSerializer


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.order_by('pk')
    serializer_class = MemberSerializer


class SessionStatusViewSet(ModelViewSet):
    queryset = SessionStatus.objects.order_by('pk')
    serializer_class = SessionStatusSerializer


class SessionViewSet(ModelViewSet):
    queryset = Session.objects.order_by('pk')
    serializer_class = SessionSerializer


class PointViewSet(ModelViewSet):
    queryset = Point.objects.order_by('pk')
    serializer_class = PointSerializer


class PromotionViewSet(ModelViewSet):
    queryset = Promotion.objects.order_by('pk')
    serializer_class = PromotionSerializer
