from rest_framework import serializers

# 定义序列化器类 跟模型models对应
from api.models import Employee, Student
from drf_day1 import settings

# 序列化器
class EmployeeSerializer(serializers.Serializer):
    '''
    需要为每一个model编写一个单独的序列化器类
    '''
    username = serializers.CharField()
    password = serializers.CharField()
    # gender = serializers.IntegerField()
    # pic = serializers.ImageField()
    phone=serializers.CharField()

    # 自定义字段 返回盐 使用SerializerMethodField来定义
    salt=serializers.SerializerMethodField()

    # 自定义字段属性名随意 但为字段提供的方法名必须是 get_字段名
    # get_字段名：是为自定义的字段提供值的方法  self是参与序列化的模型
    # 方法的返回值就是当前字段返回到前台的值
    def get_salt(self, obj):
        return "salt"

    # 自定义性别的返回值
    gender = serializers.SerializerMethodField()

    # self 是当前序列化器  obj是对象
    def get_gender(self, obj):
        # print(obj.gender, type(obj))
        # 性别是choices类型  get_字段名_display()直接访问值
        return obj.get_gender_display()

    # 自定义返回图片的全路径
    pic = serializers.SerializerMethodField()

    def get_pic(self, obj):
        # print(obj.pic)
        # http://127.0.0.1:8000/media/pic/000.jpg
        print("http://127.0.0.1:8000"+settings.MEDIA_URL + str(obj.pic))

        return "%s%s%s" % ("http://127.0.0.1:8000", settings.MEDIA_URL, str(obj.pic))


# 反序列化器
class EmployeeDeSerializer(serializers.Serializer):
    """
    反序列化：将前台提交的数据保存入库
    1. 前台需要提供哪些字段
    2. 对字段进行安全校验
    3. 哪些字段需要额外的校验
    """
    # 添加反序列化校验规则
    username = serializers.CharField(
        max_length=8,
        min_length=4,
        error_messages={
            "max_length": "长度太长了",
            "min_length": "长度太短了",
        }
    )
    password = serializers.CharField(required=False)
    phone = serializers.CharField()

    # 想要完成新增员工  必须重写create()方法
    # 继承的serializer类并没有新增做具体的实现
    def create(self, validated_data):
        # 方法中完成新增
        # print(validated_data)
        return Employee.objects.create(**validated_data)


# 学生表的序列化器
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    phone = serializers.CharField()

# 学生表的反序列化器
class StudentDeSerializer(serializers.Serializer):
    name=serializers.CharField(
        min_length=2,
        max_length=5,
        error_messages={
            "max_length": "姓名太长了",
            "min_length": "姓名太短了",
        }
    )
    age=serializers.IntegerField()
    phone=serializers.CharField()

    # 重写create()方法
    # 继承的serializer类没有对新增做具体的实现
    def create(self, validated_data):
        # 方法中完成新增
        print(validated_data)
        return Student.objects.create(**validated_data)