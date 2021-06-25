import django_filters
from django_filters import FilterSet
from rest_framework.viewsets import ModelViewSet

from .serializers import ProductTypeSerializer, HeatLevelSerializer, ProductSerializer,\
    ProductPriceSerializer, OrderDetailSerializer, SweetLevelSerializer, OrderSerializer,\
    MemberSerializer, SessionStatusSerializer, SessionSerializer, \
    ViewOrderSerializer, ViewSessionSerializer, ViewProductSerializer, ViewOrderDetailSerializer


from .models import ProductType, HeatLevel, Product, ProductPrice, OrderDetail,  \
     SweetLevel, Order, Member, SessionStatus, Session

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend



class ProductTypeViewSet(ModelViewSet):
    queryset = ProductType.objects.order_by('pk')
    serializer_class = ProductTypeSerializer


class HeatLevelViewSet(ModelViewSet):
    queryset = HeatLevel.objects.order_by('pk')
    serializer_class = HeatLevelSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.order_by('pk')
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['type', ]

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class ProductPriceViewSet(ModelViewSet):
    queryset = ProductPrice.objects.order_by('pk')
    serializer_class = ProductPriceSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['product', 'heat' ]



class OrderDetailViewSet(ModelViewSet):
    queryset = OrderDetail.objects.order_by('pk')
    serializer_class = OrderDetailSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['type']

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class SweetLevelViewSet(ModelViewSet):
    queryset = SweetLevel.objects.order_by('pk')
    serializer_class = SweetLevelSerializer


class EntryFilter(FilterSet):
    m = django_filters.NumberFilter(field_name='create_at', lookup_expr='month')
    y = django_filters.NumberFilter(field_name='create_at', lookup_expr='year')

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.order_by('pk')
    serializer_class = OrderSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # filterset_fields = ['create_at']
    filter_class = EntryFilter


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.order_by('pk')
    serializer_class = MemberSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['phone', ]


class SessionStatusViewSet(ModelViewSet):
    queryset = SessionStatus.objects.order_by('pk')
    serializer_class = SessionStatusSerializer


class SessionViewSet(ModelViewSet):
    queryset = Session.objects.order_by('pk')
    serializer_class = SessionSerializer


#------------------- View --------------------

class ViewOrderViewSet(ModelViewSet):
    queryset = Order.objects.order_by('pk')
    serializer_class = ViewOrderSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = EntryFilter

class ViewSessionViewSet(ModelViewSet):
    queryset = Session.objects.order_by('pk')
    serializer_class = ViewSessionSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['status']


class ViewProductViewSet(ModelViewSet):
    queryset = Product.objects.order_by('pk')
    serializer_class = ViewProductSerializer

class ViewOrderDetailViewSet(ModelViewSet):
    queryset = OrderDetail.objects.order_by('pk')
    serializer_class = ViewOrderDetailSerializer

