from rest_framework import serializers

# 定义序列化器类 跟模型models对应
class EmployeeSerializer(serializers.Serializer):
    '''
    需要为每一个model编写一个单独的序列化器类
    '''
    username = serializers.CharField()
    password = serializers.CharField()
    gender = serializers.IntegerField()
    pic = serializers.ImageField()