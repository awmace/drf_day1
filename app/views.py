from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from app.models import User

"""
Django视图模式两种：
FBV: 函数视图  function base view  基于函数定义的逻辑视图
CBV: 类视图    class base view     基于类定义的视图
"""


# 函数视图的定义
@csrf_exempt  # 为某个视图免除csrf认证
def user(request):
    if request.method == "GET":
        print("GET SUCCESS  查询")
        # TODO 查询用户的相关逻辑
        return HttpResponse("GET SUCCESS")

    elif request.method == "POST":
        print("POST SUCCESS  添加")
        # TODO 添加用户的相关的逻辑
        return HttpResponse("POST SUCCESS")

    elif request.method == "PUT":
        print("PUT SUCCESS  修改")
        return HttpResponse("PUT SUCCESS")

    elif request.method == "DELETE":
        print("DELETE SUCCESS  删除")
        return HttpResponse("DELETE SUCCESS")



"""
单条：获取单条  获取所有  添加单个  删除单个  整体更新单个  局部更新单个
群体：增加多个  删除多个  整体修改多个   局部修改多个
"""

# 类视图的定义
@method_decorator(csrf_exempt, name="dispatch")  # 让类视图免除csrf认证
class UserView(View):
    """
    类视图内部通过请求的方法来匹配到对应的内部的函数，从而进行对应的处理
    """

    def get(self, request, *args, **kwargs):
        """
                提供查询单个用户与多个用户的操作
                :param request:  用户id
                :return: 查询后的用户信息
                """

        # 获取用户id
        user_id=kwargs.get('id')
        if user_id:
            user=User.objects.filter(pk=user_id).values("username", "password", "gender").first()
            if user:
                # 如果查询出对应的用户信息，则返回给前端
                return JsonResponse({
                    'status':200,
                    'message':'查询单个用户成功',
                    'results':user,
                })
        else:
            # 如果没有传参数id  代表查询所有
            user_list = User.objects.all().values("username", "password", "gender")
            print(type(user_list))
            if user_list:
                return JsonResponse({
                    "status": 200,
                    "message": "查询所有用户成功",
                    "results": list(user_list),
                })
        return JsonResponse({
            "status": 500,
            "message": "查询失败",
        })

    def post(self, request, *args, **kwargs):
        """
            新增单个用户
        """
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        print(username,pwd)
        try:
            user_obj = User.objects.create(username=username, password=pwd)
            return JsonResponse({
                "status": 201,
                "message": "创建用户成功",
                "results": {"username": user_obj.username, "gender": user_obj.gender}
            })
        except:
            return JsonResponse({
                "status": 500,
                "message": "创建用户失败",
            })
    def put(self, request, *args, **kwargs):
        print("PUT SUCCESS  修改")
        return HttpResponse("PUT SUCCESS")

    def delete(self, request, *args, **kwargs):
        print("DELETE SUCCESS  删除")
        return HttpResponse("DELETE SUCCESS")


from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

class UserAPIView(APIView):
    def get(self,request,*args,**kwargs):

        # 可以通过_request 访问Django原生的request对象
        print(request._request.GET)
        # 通过DRF 的request对象获取参数
        print(request.GET)
        # 通过quer_params来获取参数
        print(request.query_params)

        # 获取路径传参
        user_id = kwargs.get("id")
        if user_id:
            user = User.objects.filter(pk=user_id).values("username", "password", "gender").first()
            if user:
                # 如果查询出对应的用户信息，则返回给前端
                return JsonResponse({
                    'status': 200,
                    'message': '查询单个用户成功',
                    'results': user,
                })
        else:
            # 如果没有传参数id  代表查询所有
            user_list = User.objects.all().values("username", "password", "gender")
            print(type(user_list))
            if user_list:
                return JsonResponse({
                    "status": 200,
                    "message": "查询所有用户成功",
                    "results": list(user_list),
                })
        return JsonResponse({
            "status": 500,
            "message": "查询失败",
        })




    def post(self,request,*args,**keargs):
        # post请求传递参数的形式  form-data  www-urlencoded  json
        print(request._request.POST)  # Django 原生的request对象
        print(request.POST)  # DRF 封装后的request对象
        # 可以获取多种格式的参数 DRF 扩展的请回去参数  兼容性最强
        print(request.data)

        username = request.POST.get("username")
        pwd = request.POST.get("password")
        print(username, pwd)
        try:
            user_obj = User.objects.create(username=username, password=pwd)
            return JsonResponse({
                "status": 201,
                "message": "创建用户成功",
                "results": {"username": user_obj.username, "gender": user_obj.gender}
            })
        except:
            return JsonResponse({
                "status": 500,
                "message": "创建用户失败",
            })