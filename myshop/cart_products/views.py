
from rest_framework import viewsets
from cart_products.models import Cart_product
from cart_products.serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated
from cart_products.permissions import IsOwner
from rest_framework.response import Response


# Create your views here.


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart_product.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = request.user.cart.all()
        serializer = CartSerializer(queryset, many=True)

        print(serializer.data)
        return Response(serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        if pk == '0':
            Cart_product.objects.filter(user=request.user).delete()
            return Response('Корзина очищена')
        else:
            return super(CartViewSet, self).destroy(request, pk, *args, **kwargs)


