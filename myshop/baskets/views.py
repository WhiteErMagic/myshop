
from rest_framework import viewsets
from baskets.models import Basket
from rest_framework.permissions import IsAuthenticated
from baskets.permissions import IsOwner
from rest_framework.response import Response
from baskets.serializers import BasketSerializer, BasketGoodSerializer
from baskets.models import BasketGood



# Create your views here.

class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def list(self, request, *args, **kwargs):
        queryset = BasketGood.objects.filter(basket__user=request.user)
        serializer = BasketSerializer(queryset, many=True)

        return Response(serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        if pk == '0':
            BasketGood.objects.filter(basket__user=request.user).delete()
            return Response('Корзина очищена')
        else:
            return super(BasketViewSet, self).destroy(request, pk, *args, **kwargs)


class BasketGoodViewSet(viewsets.ModelViewSet):
    queryset = BasketGood.objects.all()
    serializer_class = BasketGoodSerializer

    def perform_create(self, serializer):
        obj, created = Basket.objects.get_or_create(user=self.request.user)
        serializer.save(basket=obj)