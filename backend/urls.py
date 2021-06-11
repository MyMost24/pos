from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()

router.register(r'producttype', views.ProductTypeViewSet)
router.register(r'heatlevel', views.HeatLevelViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'productprice', views.ProductPriceViewSet)
router.register(r'productpriceview', views.ViewProductPriceViewSet)
router.register(r'orderdetailtype', views.OrderDetailTypeViewSet)
router.register(r'orderdetail', views.OrderDetailViewSet)
router.register(r'sweetlevel', views.SweetLevelViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'member', views.MemberViewSet)
router.register(r'sessionstatus', views.SessionStatusViewSet)
router.register(r'session', views.SessionViewSet)
router.register(r'point', views.PointViewSet)
router.register(r'promotion', views.PromotionViewSet)

urlpatterns = router.urls
