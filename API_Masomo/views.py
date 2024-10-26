from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *
from rest_framework import authentication, generics, mixins, permissions
from .permissions import *
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from django.contrib.auth import logout
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate, login
# Create your views here.


class EtablissemntView_3(generics.ListAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.AllowAny]
    queryset = Etablissement.objects.all().order_by('?')[:3]
    serializer_class = EtablissementSerializer

class LoginView(generics.ListCreateAPIView):
    
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"Msg": "Connected !" ,"token": token.key})
        else:
            return Response({"error": "Identifiant invalid"})



class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)


class EtablissemntView_6(generics.ListAPIView):
    
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Etablissement.objects.all().order_by('?')[:6]
    serializer_class = EtablissementSerializer


class UserMixin(generics.GenericAPIView,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin):
    
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):

        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):

        return self.destroy(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):

        return self.partial_update(request, *args, **kwargs)
       
class MasomoMixin(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin
):
    queryset = Etablissement.objects.all()
    serializer_class = EtablissementSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('designationEcole')
        email = request.data.get('email')



        if User.objects.filter(username=username).exists():
            return Response({"error": "User with this username already exists."})
    
        # Create user
        user = User.objects.create_user(
            username=username,
            password="1234",
            email=email
            )
        #le statut is_staff
        user.is_staff = True
        user.save()

        etablissement = Etablissement.objects.create(
            user=user,
            image=request.data.get('image'),
            designationEcole=username,
            arreteMin=request.data.get('arreteMin'),
            adresse=request.data.get('adresse'),
            telephone=request.data.get('telephone'),
            email=email,
            typesEcole=request.data.get('typesEcole'),
            degree=request.data.get('degree'),
            promoteur=request.data.get('promoteur'),
            biographie=request.data.get('biographie')
        )

        serializer = EtablissementSerializer(etablissement)
        return Response(serializer.data)

    
    
    def put(self, request, *args, **kwargs):

        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):

        return self.destroy(request, *args, **kwargs)
  

class MasomoClasseMixin(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin
    ):
    
    queryset = MasomoClasse.objects.all()
    serializer_class = MasomoClasseSerializer
    lookup_field = 'pk'
    
    
    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)
    
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Ajoutez des revendications personnalisées
        token['username'] = user.username
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
     
        
    
