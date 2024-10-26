from django.urls import path
from .views import *


urlpatterns = [
    #Pour Trois
    path('', EtablissemntView_3.as_view()),
    #Pour Six
    path('Masomo_Alea_6', EtablissemntView_6.as_view()),
    # List all users
    path('List-User/', UserMixin.as_view()),
    #LogIn 
    path('login/', LoginView.as_view()),

    path('Token/', CustomTokenObtainPairView.as_view()),
    #LogOut
    path('LogOut/', LogoutView.as_view()),
    # Insert school and user ===> default username = nameschool and pwd = 1234 
    path('Insert-Masomo/', MasomoMixin.as_view()),
    # Update school
    path('Update-Masomo/<int:pk>/', MasomoMixin.as_view()),
    # Delete school
    path('Delete-Masomo/<int:pk>/', MasomoMixin.as_view()),
]
