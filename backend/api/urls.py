from django.urls import include, path
from . import views

urlpatterns = [
    path('welcome', views.welcome),
    path('users', views.users),
    
    #API DE EMPRESAS
    path('getcompanies', views.get_companies),
    path('addcompany', views.add_company),
    path('updatecompany/<int:company_id>', views.update_company),
    path('deletecompany/<int:company_id>', views.delete_company),


    #API DE DENÚNCIAS
    path('getdenuncias', views.get_denuncias),
    path('adddenuncia', views.add_denuncia),
    path('updatedenuncia/<int:denuncia_id>', views.update_denuncia),
    path('deletedenuncia/<int:denuncia_id>', views.delete_denuncia),

]