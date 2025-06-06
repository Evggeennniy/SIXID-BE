from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import RegisterSerializer
from django.contrib.auth import login


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'ok'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
