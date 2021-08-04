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

    #API DE CADASTROS
    path('getcadastros', views.get_cadastros),
    path('addcadastro', views.add_cadastro),
    path('updatecadastro/<int:cadastro_id>', views.update_cadastro),
    path('deletecadastro/<int:cadastro_id>', views.delete_cadastro),

    #API DE PONTOS DE COLETA
    path('getpontosDeColetas', views.get_pontosDeColetas),
    path('addpontosDeColeta', views.add_pontosDeColeta),
    path('updatepontosDeColeta/<int:pontosDeColeta_id>', views.update_pontosDeColeta),
    path('deletepontosDeColeta/<int:pontosDeColeta_id>', views.delete_pontosDeColeta),

]
