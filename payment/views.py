from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    CreateCheckoutSessionSerializer,
)


class CreateCheckoutSession(APIView):
    def get(self, request, pk, *args, **kwargs):
        serializer = CreateCheckoutSessionSerializer(
            data=request.data, context={'request': request, 'pk': pk}
        )
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            if data is not False:
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
