from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GoodsViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('goods', GoodsViewSet)

urlpatterns = router.urls
