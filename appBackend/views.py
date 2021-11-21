from django.http.response import JsonResponse
from rest_framework.response import Response
from django.views import generic
from rest_framework import viewsets
from users.models import CustomUser
from .serializers import UserSerializer
from rest_framework import permissions



class LoginView(generic.TemplateView):
  template_name = 'appBackend/login.html'

class MenuView(generic.TemplateView):
  template_name = 'appBackend/menu.html'


class MyProfileApi(viewsets.ModelViewSet):
  serializer_class = UserSerializer
  queryset = CustomUser.objects.all()
  # permission_classes = [permissions.IsAuthenticated]
  # renderer_classes = [JSONRenderer]

  # @action(detail=False, methods=['get'])
  # def getMyProfile(self, request, pk):
  #   data = super().get_queryset()
  #   serialized = UserSerializer(data, many=True)
  #   return Response(serialized.data)
