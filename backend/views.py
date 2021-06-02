from rest_framework.viewsets import ModelViewSet

from .serializers import ProductTypeSerializer, HeatLevelSerializer, ProductSerializer,\
    ProductPriceSerializer, OrderDetailSerializer, CoffeeToppingSerializer, TeaToppingSerializer,\
    SweetLevelSerializer, OrderSerializer, MemberSerializer, SessionStatusSerializer, SessionSerializer,\
    PointSerializer, PromotionSerializer, ViewProductPriceSerializer

from .models import ProductType, HeatLevel, Product, ProductPrice, OrderDetail, CoffeeTopping, \
    TeaTopping, SweetLevel, Order, Member, SessionStatus, Session, Point, Promotion


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
#------------------------------
class ViewProductPriceViewSet(ModelViewSet):
    queryset = ProductPrice.objects.order_by('pk')
    serializer_class = ViewProductPriceSerializer
#------------------------------
class OrderDetailViewSet(ModelViewSet):
    queryset = OrderDetail.objects.order_by('pk')
    serializer_class = OrderDetailSerializer


class CoffeeToppingViewSet(ModelViewSet):
    queryset = CoffeeTopping.objects.order_by('pk')
    serializer_class = CoffeeToppingSerializer


class TeaToppingViewSet(ModelViewSet):
    queryset = TeaTopping.objects.order_by('pk')
    serializer_class = TeaToppingSerializer


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
