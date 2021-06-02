from django.contrib import admin

from .models import ProductType, Member, SessionStatus, Session, Point, Promotion,\
    OrderDetail, CoffeeTopping, TeaTopping, SweetLevel, Order, HeatLevel, Product, ProductPrice

from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

# Register your models here.

class ProductDetailChildAdmin(PolymorphicChildModelAdmin):

    base_model = OrderDetail


@admin.register(CoffeeTopping)
class ToppingAdmin(ProductDetailChildAdmin):
    base_model = CoffeeTopping\

@admin.register(TeaTopping)
class ToppingAdmin(ProductDetailChildAdmin):
    base_model = TeaTopping


@admin.register(OrderDetail)
class ProductDetailAdmin(PolymorphicParentModelAdmin):
    base_model = OrderDetail
    child_models = (CoffeeTopping, TeaTopping)

class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ['detail']

class SessionAdmin(admin.ModelAdmin):
    filter_horizontal = ['order']


admin.site.register(Order, OrderAdmin)
admin.site.register(Member)
admin.site.register(SweetLevel)
admin.site.register(SessionStatus)
admin.site.register(Session, SessionAdmin)
admin.site.register(Point)
admin.site.register(Promotion)

admin.site.register(HeatLevel)
admin.site.register(ProductType)
admin.site.register(ProductPrice)


class PriceInline(admin.TabularInline):
    model = ProductPrice
    fk_name = "product"
    # filter_horizontal = ('choice',)
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra

class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceInline, ]


admin.site.register(Product, ProductAdmin)
