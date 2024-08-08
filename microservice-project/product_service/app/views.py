from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from app.uitlity import capture_error
from app.models import Product
# Create your views here.



class DictToObject:
    def __init__(self, dict_obj):
        for key, value in dict_obj.items():
            setattr(self, key, value)


class ProductService:

    def request_validator(self,data:dict) -> object:
        keys = ["name","price"]
        for i in keys:
            if i not in data:
                raise ValueError(f"'{i}' parameter is missing")
        return DictToObject(data)



    def create(self,data)->dict:
        create_product = Product.objects.create(name=data.name,price=data.price)
        return {"message":"created"}

    def get_products(self,page_no:int=1,page_length:int=10)->list:
        end_point = page_length*page_no
        start_point = end_point-page_length
        record = Product.objects.values("id","name","price")[start_point:end_point]
        recordList = []
        for i in record:
            recordList.append({"id":i["id"],"name":i["name"],"price":i["price"]})
        return recordList
    
    def get_product(self,pk):
        record = Product.objects.get(pk=pk)
        record = {"id":record.id,"name":record.name,"created_at":str(record.created_at)}
        return record



@api_view(["POST"])
@capture_error
def create_procuct(request):
    request_data = request.data
    service = ProductService()
    response = service.create(service.request_validator(request_data))
    return JsonResponse(response,status=201)


@api_view(["GET"])
@capture_error
def get_products(request):
    page_no = int(request.GET.get("page_no",1))
    page_length = int(request.GET.get("page_length",10))
    service = ProductService()
    response = service.get_products(page_no,page_length)
    return JsonResponse(response,status=200,safe=False)

@api_view(["GET"])
@capture_error
def get_product(request):
    pk = request.GET.get("id",None)
    if not pk:
        raise ValueError("'id' parameter is missing")
    service = ProductService()
    response = service.get_product(pk)
    return JsonResponse(response,status=200)