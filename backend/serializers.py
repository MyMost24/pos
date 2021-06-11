from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import ProductType, HeatLevel, Product, ProductPrice, OrderDetail, \
    SweetLevel, Order, Member, SessionStatus, Session, Point, Promotion, OrderDetailType


class ProductTypeSerializer(ModelSerializer):

    class Meta:
        model = ProductType
        fields = '__all__'


class HeatLevelSerializer(ModelSerializer):

    class Meta:
        model = HeatLevel
        fields = '__all__'


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductPriceSerializer(ModelSerializer):

    class Meta:
        model = ProductPrice
        fields = '__all__'

class ViewProductPriceSerializer(ModelSerializer):
    # product = ProductSerializer(read_only=True)
    # heat = HeatLevelSerializer(read_only=True)
    named = SerializerMethodField()
    class Meta:
        model = ProductPrice
        fields = '__all__'
    def get_named(self,obj):
        try:
            heat = HeatLevel.objects.get(id=obj.heat_id)
            return heat.name
        except:
            return None

class OrderDetailTypeSerializer(ModelSerializer):

    class Meta:
        model = OrderDetailType
        fields = '__all__'


class OrderDetailSerializer(ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = '__all__'



class SweetLevelSerializer(ModelSerializer):

    class Meta:
        model = SweetLevel
        fields = '__all__'


class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class MemberSerializer(ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'


class SessionStatusSerializer(ModelSerializer):

    class Meta:
        model = SessionStatus
        fields = '__all__'


class SessionSerializer(ModelSerializer):

    class Meta:
        model = Session
        fields = '__all__'


class PointSerializer(ModelSerializer):

    class Meta:
        model = Point
        fields = '__all__'


class PromotionSerializer(ModelSerializer):

    class Meta:
        model = Promotion
        fields = '__all__'
