from django.db import models

# Create your models here.


class UserInfo(models.Model):
    #ID列，自增，主键
    #用户名列，字符串类型，指定长度
    username = models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    email = models.CharField(max_length=60)
    age = models.IntegerField(default=25)
    gender = models.CharField(max_length=20, default='男')

    user_type_choices = (
        (1, '管理用户'),
        (2, '普通用户'),
        (3, '临时用户')
    )

    user_group = models.ForeignKey("UserGroup", to_field='uid', on_delete=models.CASCADE,default=1)
    user_type_id = models.IntegerField(choices=user_type_choices,default=1)



class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32, unique=True)
    ctime = models.DateTimeField(auto_now_add=True, null=True)
    uptime = models.DateTimeField(auto_now=True, null=True)
