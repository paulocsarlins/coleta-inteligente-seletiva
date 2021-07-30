from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from .serializers import CompanySerializer
from .models import Company
import json
from django.core.exceptions import ObjectDoesNotExist

@api_view(["GET"])
def welcome(request):
    content = {"message": "Minha primeira view em Django!"}
    return JsonResponse(content)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def users(request):
    users = [
        {'name':'Paulo','email':'paulo@gmail.com'}
    ]

    return JsonResponse(users, safe=False)


#API PARA EMPRESAS: LISTAR, ADICIONAR, REMOVER E EDITAR

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_companies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return JsonResponse({'companies': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_company(request):
    payload = json.loads(request.body)
    try:
        company = Company.objects.create(
            name=payload["name"],
            cnpj=payload["cnpj"],
            companyType=payload["companyType"],
            address=payload["address"],
        )
        serializer = CompanySerializer(company)
        return JsonResponse({'company': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Erro ao adicionar'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
        company.delete()
        serializer = CompanySerializer(company)
        return JsonResponse({'company': serializer.data}, safe=False, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_company(request, company_id):
    payload = json.loads(request.body)
    try:
        company_item = Company.objects.filter(id=company_id)
        # returns 1 or 0
        company_item.update(**payload)
        company = Company.objects.get(id=company_id)
        serializer = CompanySerializer(company)
        return JsonResponse({'company': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Erro ao editar'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)