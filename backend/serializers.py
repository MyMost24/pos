from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import ProductType, HeatLevel, Product, ProductPrice, OrderDetail, \
    SweetLevel, Order, Member, SessionStatus, Session


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
    heat_named = SerializerMethodField()
    product_named = SerializerMethodField()
    class Meta:
        model = ProductPrice
        fields = '__all__'

    def get_product_named(self, obj):
        try:
            product = Product.objects.get(id=obj.product_id)
            return product.name
        except:
            return None


    def get_heat_named(self, obj):
        try:
            heat = HeatLevel.objects.get(id=obj.heat_id)
            return heat.name
        except:
            return None


class OrderDetailSerializer(ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = '__all__'

    def get_named(self,obj):
        try:
            type = ProductType.objects.get(id=obj.type_id)
            return type.name
        except:
            return None


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

    def get_phone(self,obj):
        try:
            phone = Member.objects.get(id=obj.phone_member)
            return phone.name
        except:
            return None


class SessionStatusSerializer(ModelSerializer):

    class Meta:
        model = SessionStatus
        fields = '__all__'


class SessionSerializer(ModelSerializer):

    class Meta:
        model = Session
        fields = '__all__'


#---------------view--------------------------

class ViewProductSerializer(ModelSerializer):
    type = ProductTypeSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'



class ViewOrderDetailSerializer(ModelSerializer):
    type = ProductTypeSerializer(read_only=True, many=True)
    class Meta:
        model = OrderDetail
        fields = '__all__'


class ViewOrderSerializer(ModelSerializer):
    product = ProductPriceSerializer(read_only=True)
    detail = OrderDetailSerializer(read_only=True, many=True)
    sweetlevel = SweetLevelSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class ViewSessionSerializer(ModelSerializer):
    member = MemberSerializer(read_only=True)
    order = ViewOrderSerializer(read_only=True, many=True)
    status = SessionStatusSerializer(read_only=True)

    class Meta:
        model = Session
        fields = '__all__'

