from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from library.models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from datetime import datetime

# Create your views here.

def not_supportedMethod():
    data = {'error':    'Method Not Supported',
            'status':405
            }
    return JsonResponse(data,safe=False,status=405)

@method_decorator(csrf_exempt, name='dispatch')
def lib_upsert(req):
    if req.method=='POST': 
        data=json.loads(req.body.decode())
        output= []
        expected_format=[
                        {"name":"Library2",
                            "city": "Kadapa",
                            "state": "AP",
                            "postal_code": "5167003"
                        }]
        fields = set(expected_format[0].keys())
        error_data={
                        "status": 422,
                        "error":"Request body is not in expected format",
                        "expectedformat": expected_format,
                        "exptectedKeys": list(fields),
                        "recievedFormat":data
                    }
        if list == type(data):
            for val in data:
                print("*"*20)
                print(set(val.keys()) - fields and  fields - set(val.keys()))
                if len(val.keys()) != len(fields) or (set(val.keys()) - fields and  fields - set(val.keys())) != set():
                    return JsonResponse(error_data,safe=False,status=422)
        else: 
                    return JsonResponse(error_data,safe=False,status=422)
        for val in data: 
            lib=Libraries(**val)
            lib.save()
            output.append({'book_id':lib.library_id,'author_name':val['name'],
            'status':'created Sucessfully'})
        return JsonResponse(output,safe=False,status=201)
    return not_supportedMethod()

def lib_getAll(req):
    if req.method== 'GET':
        data=Libraries.objects.values()
        return JsonResponse(list(data),safe=False)
    return not_supportedMethod()
def lib_get(req,lib_id):
    if req.method== 'GET':
        data=Libraries.objects.get(library_id=lib_id)
        
        return JsonResponse(data,safe=False)
    return not_supportedMethod()

@method_decorator(csrf_exempt, name='dispatch')
def books_upsert(req):
    if req.method=='POST': 
        data=json.loads(req.body.decode())
        output= []
        expected_format=[{"title":"Test 2",
                        "author_name": "Test Author22",
                        "genre": "test genre2",
                        "isbn_num": "121-2323-224",
                        "description": "Thsis is sample description2"
                    }]
        fields = {'title', 'author_name', 'genre', 'isbn_num', 'description'}
        error_data={
                        "status": 422,
                        "error":"Request body is not in expected format",
                        "expectedformat": expected_format,
                        "exptectedKeys": fields,
                        "recievedFormat":data
                    }
        if list == type(data):
            for val in data:
                if len(val.keys()) != len(fields) or (set(val.keys()) - fields and  fields - set(val.keys())) != set():
                    return JsonResponse(error_data,safe=False,status=422)
        else: 
                    return JsonResponse(error_data,safe=False,status=422)
        for val in data: 
            books=Books(**val)
            books.save()
            output.append({'book_id':books.book_id,'author_name':val['author_name'],
            'status':'created Sucessfully'})
        return JsonResponse(output,safe=False,status=201)
    return not_supportedMethod()

def books_getAll(req):
    if req.method== 'GET':
        data = Books.objects.values()
        return JsonResponse(list(data),safe=False)
    return not_supportedMethod()

def books_get(req,book_id):
    if req.method== 'GET':
        data=list(Books.objects.filter(book_id=book_id).values())
        return JsonResponse(data,safe=False)
    return not_supportedMethod()

def library_book_get_checkout_bylibrary(req,library_id):
    if req.method== 'GET':
        lib_act = list(Library_Activities.objects.filter(library_book_id__library_id=library_id,check_out_at__isnull=False).values('library_book_id__book_id__author_name'))
        return JsonResponse(lib_act,safe=False)
    return not_supportedMethod()

def library_book_get_checkout_byuser(req,user_id):
    if req.method== 'GET':
        lib_act = list(Library_Activities.objects.filter(user_id__id=user_id,check_in_at__isnull =False).values('library_book_id__book_id__author_name','library_book_id__book_id__book_id'))
        return JsonResponse(lib_act,safe=False)
    return not_supportedMethod()

def library_book_checkin(req,book_id,user_id):
    if req.method== 'POST':
        try:
            lib_act = Library_Activities.objects.get(library_book_id=book_id,user_id=user_id)
        except Exception as e:
            lib_act = None    
        if lib_act:
            lib_act.check_in_at = datetime.now()
            lib_act.save()
        else: 
            user = Users.objects.get(id=user_id)
            lib_book = Library_Books.objects.get(book_id=book_id)
            lib_act=Library_Activities(check_in_at=datetime.now(),user_id=user,library_book_id=lib_book,check_out_at=datetime.now())
            lib_act.save()
        return JsonResponse(lib_act.library_activity_id,safe=False)
    return not_supportedMethod()
    

def library_book_checkout(req,book_id,user_id):
    if req.method== 'POST':
        lib_act = Library_Activities.objects.get(library_book_id=book_id)
        return JsonResponse(lib_act,safe=False)
    return not_supportedMethod()
    

def library_book_create(req,library_id):
    if req.method=='POST': 
        data=json.loads(req.body.decode())
        output= []
        expected_format=[
                    {"book_id": 123
                    }]
        fields = {'book_id'}
        error_data={
                        "status": 422,
                        "error":"Request body is not in expected format",
                        "expectedformat": expected_format,
                        "exptectedKeys": fields,
                        "recievedFormat":data
                    }
        if list == type(data):
            for val in data:
                if len(val.keys()) != len(fields) or (set(val.keys()) - fields and  fields - set(val.keys())) != set():
                    return JsonResponse(error_data,safe=False,status=422)
        else: 
                    return JsonResponse(error_data,safe=False,status=422)
        for val in data: 
            lib_id = Libraries.objects.get(library_id=library_id)
            book_id= Books.objects.get(book_id= val['book_id'])
            lib_books=Library_Books(library_id=lib_id,book_id=book_id)
            lib_books.save()
            output.append({'book_id':lib_books.library_book_id,
            'status':'created Sucessfully'})
        return JsonResponse(output,safe=False,status=201)
    return not_supportedMethod()