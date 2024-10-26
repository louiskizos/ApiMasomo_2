from hashlib import sha3_256
from rest_framework import serializers, authentication
from .models import *
from django.contrib.auth.models import User

class EtablissementSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user', read_only=True)

    class Meta:
        model = Etablissement
        fields = ('pk','user_name','image', 'designationEcole', 'arreteMin', 'adresse', 'telephone', 'email', 'typesEcole', 'degree', 'promoteur', 'biographie')

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('pk','username','password', 'email')

class MasomoClasseSerializer(serializers.ModelSerializer):
    masomo_name = serializers.CharField(source='etablissement', read_only=True)
    
    class Meta:
        model = MasomoClasse
        fields = ('pk','masomo_name','designationClasse')

class MasomoSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasomoSection
        fields = ('pk','classeMasomo','designationSection')
        

class MasomoOptionSelializer(serializers.ModelSerializer):
    
    class Meta:
        model = MasomoOption
        
        fields = ('pk','sectionMasomo','designationOption')