from rest_framework.response import Response
from rest_framework.serializers import Serializer

from rest_framework.views import APIView

from api.models import Employee
from .serializers import EmployeeSerializer

class EmployeeAPIView(APIView):
    def get(self,request,*args,**kwargs):
        user_id=kwargs.get('pk')
        if user_id:
            #查询单个
            emp_obj=Employee.objects.get(pk=user_id)
            # 查询的当员工数据无法直接序列化，需要使用序列化器
            emp_ser=EmployeeSerializer(emp_obj).data
            return Response({
                'status':200,
                'msg':'查询单个员工成功',
                'result':emp_ser,
            })
        else:
            #查询所有
            # 员工对象无法直接序列化
            emp_list = Employee.objects.all()
            return Response({
                'status': 200,
                'msg': '查询所有员工成功',
                'result': list(emp_list),
            })