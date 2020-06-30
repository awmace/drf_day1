from rest_framework.response import Response
from rest_framework.serializers import Serializer

from rest_framework.views import APIView

from api.models import Employee, Student
from .serializers import EmployeeSerializer, EmployeeDeSerializer, StudentSerializer, StudentDeSerializer


class EmployeeAPIView(APIView):
    def get(self,request,*args,**kwargs):
        user_id = kwargs.get('id')
        print(user_id)
        if user_id:
            # 查询单个
            emp_obj = Employee.objects.get(pk=user_id)
            # 查询的当员工数据无法直接序列化，需要使用序列化器
            # .data:将序列化器的数据打包成字典
            emp_obj = EmployeeSerializer(emp_obj).data

            return Response({
                'status':200,
                'msg':'查询单个员工成功',
                'result':emp_obj,
            })
        else:
            #查询所有
            # 员工对象无法直接序列化
            emp_list = Employee.objects.all()
            # 使用序列化器完成所有员工的序列化 需要指定参数many=True,默认是False
            emp_list=EmployeeSerializer(emp_list,many=True).data
            return Response({
                'status': 200,
                'msg': '查询所有员工成功',
                'result': emp_list,
            })

    # 添加数据
    def post(self, request, *args, **kwargs):
        '''
        新增单个数据
        '''
        user_data=request.data
        #  前端发送的数据需要入库时  必须对前台的数据进行校验
        if not isinstance(user_data, dict) or user_data == {}:
            return Response({
                "status": 501,
                "msg": "数据有误",
            })
        # 使用序列化器对前台提交的数据进行反序列化
        # 在反序列化时需要指定关键字参数  data
        serializer = EmployeeDeSerializer(data=user_data)
        # print(serializer)
        # print(serializer.is_valid())
        # # 对序列化的数据进行校验  通过is_valid() 方法对传递过来的参数进行校验  校验合法返回True
        if serializer.is_valid():
            # 调用save()去保存对象  必须重写create()方法
            # create() 方法保存成功后会返回 员工实例
            emp_obj = serializer.save()
            # 将创建成功的用户实例返回到前端
            return Response({
                "status": 201,
                "msg": "用户创建成功",
                "results": EmployeeSerializer(emp_obj).data
            })
        else:
            return Response({
                "status": 501,
                "msg": "用户创建失败",
                # 验证失败后错误信息包含在 .errors中
                "results": serializer.errors
            })


class StudentAPIView(APIView):
    def get(self,request,*args,**kwargs):
        stu_id = kwargs.get('id')
        print(stu_id)
        if stu_id:
            # 查询单个
            stu_obj = Student.objects.get(pk=stu_id)
            # 查询的当员工数据无法直接序列化，需要使用序列化器
            # .data:将序列化器的数据打包成字典
            stu_obj = StudentSerializer(stu_obj).data

            return Response({
                'status': 200,
                'msg': '查询单个学生成功',
                'result': stu_obj,
            })
        else:
            # 查询所有
            # 员工对象无法直接序列化
            stu_list = Student.objects.all()
            # 使用序列化器完成所有员工的序列化 需要指定参数many=True,默认是False
            stu_list = StudentSerializer(stu_list, many=True).data
            return Response({
                'status': 200,
                'msg': '查询所有学生成功',
                'result': stu_list,
            })

    def post(self,request,*args,**kwargs):
        stu_data = request.data
        #  前端发送的数据需要入库时  必须对前台的数据进行校验
        if not isinstance(stu_data, dict) or stu_data == {}:
            return Response({
                "status": 501,
                "msg": "数据有误",
            })
        # 使用序列化器对前台提交的数据进行反序列化
        # 在反序列化时需要指定关键字参数  data
        serializer = StudentDeSerializer(data=stu_data)
        # print(serializer)
        print(serializer.is_valid())
        # # 对序列化的数据进行校验  通过is_valid() 方法对传递过来的参数进行校验  校验合法返回True
        if serializer.is_valid():
            # 调用save()去保存对象  必须重写create()方法
            # create() 方法保存成功后会返回 员工实例
            stu_obj = serializer.save()
            # 将创建成功的用户实例返回到前端
            return Response({
                "status": 201,
                "msg": "用户创建成功",
                "results": StudentSerializer(stu_obj).data
            })
        else:
            return Response({
                "status": 501,
                "msg": "用户创建失败",
                # 验证失败后错误信息包含在 .errors中
                "results": serializer.errors
            })


