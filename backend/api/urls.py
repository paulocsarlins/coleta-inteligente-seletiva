from django.urls import include, path
from . import views

urlpatterns = [
    path('welcome', views.welcome),
    path('users', views.users),
    
    #API DE EMPRESAS
    path('getcompanies', views.get_companies),
    path('addcompany', views.add_company),
    path('updatecompany/<int:company_id>', views.update_company),
    path('deletecompany/<int:company_id>', views.delete_company)

]