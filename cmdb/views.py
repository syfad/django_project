from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from utils import pagination

import pymysql
import json


from cmdb import models


def login(request):
    from app02 import models
    error_msg = ''
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        # 获取用户通过post提交过来的数据
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        obj = models.UserInfo.objects.filter(username=user,password=pwd).first()
        if obj:

            res = redirect('/cmdb/modelbox/')

            #设置cookie，max_age多少秒之后失效
            res.set_cookie('username_cookie', user, max_age=600)

            return res
        else:
            error_msg = "用户名密码错误"
    return render(request, 'login.html', {'error_msg': error_msg})


def register(request):
    # return render(request, 'register.html')
    return redirect('/cmdb/modelbox/')


def home(request):
    USER_LIST = [
        {'username': 'syf', 'email': 'syf@123.com', 'gender': '男'},
        {'username': 'eric', 'email': 'eric@123.com', 'gender': '男'},
        {'username': 'seven', 'email': 'seven@123.com', 'gender': '男'}
    ]
    # for index in range(5):
    #     temp = {'username': 'syf'+ str(index), 'email': 'syf@123.com', 'gender': '男'}
    #     USER_LIST.append(temp)

    if request.method == "POST":
        n = request.POST.get('num')
        u = request.POST.get('username')
        e = request.POST.get('email')
        g = request.POST.get('gender')
        temp = {'username': u, 'email': e, 'gender': g}
        USER_LIST.append(temp)

    return render(request, 'home.html', {'user_list': USER_LIST})


def modelbox(request):
    v = request.COOKIES.get('username_cookie')
    if not v:
        return redirect('/cmdb/login/')
    else:
        current_page = request.GET.get('p', 1)
        current_page = int(current_page)
        val = request.COOKIES.get('per_page_count', 10)
        val = int(val)

        db = pymysql.connect("192.168.100.198", "django", "123456", "django")
        # cursor = db.cursor()
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT COUNT(*) FROM user")
        data_count = cursor.fetchone()
        count = data_count['COUNT(*)']

        page_obj = pagination.Page(current_page, count, val)


        cursor.execute("select * from user limit %s, %s" %(page_obj.start, page_obj.end))
        print(page_obj.start,page_obj.end)

        data = cursor.fetchall()

        page_str = page_obj.page_str("/cmdb/modelbox/")

        cursor.close()
        db.close()
    return render(request, 'modelbox.html',{'data_list': data, 'page_str': page_str})


# 查看详细：
def detail(request, uid):
    # uid = request.GET.get("nid")
    db = pymysql.connect("192.168.100.198", "django", "123456", "django")
    # cursor = db.cursor()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select * from user where id=%s" % (uid))
    data = cursor.fetchall()
    #print(data)
    db.close()
    return render(request, 'detail.html', {'list': data})


def index(request, uid, nid):
    print(uid, nid)
    print(request.path_info)

    from django.urls import reverse
    # v = reverse('indexx', args=(90,88,))
    v = reverse('indexx', args={"nid": 1, 'uid': '99'})
    print(v)
    return HttpResponse('<h1>welcome to CMDB pages</h1>')

def useredit(request, nid):
    db = pymysql.connect("192.168.100.198", "django", "123456", "django")

    if request.method == "GET":
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute(" select * from user where id=%s" %(nid))
        data = cursor.fetchall()
        db.close()
        return render(request, 'useredit.html', {'data': data})

    elif request.method == "POST":
        id = request.POST.get('id')
        age = request.POST.get('age')
        username = request.POST.get('user')
        pwd = request.POST.get('pwd')
        gender = request.POST.get('gender')
        email = request.POST.get('email')

        id = int(id)
        age = int(age)

        cursor = db.cursor()
        #使用的pymysql在插入数据的时候，如果是vchar类型的，需要加入单引号，即name = "'door'"，其中还要有一个引号，对应矩阵存储，要先用str()进行转化，然后在加单引号才能成功。python里面提供了repr()函数可以自动将其加上引号
        sql = "update user set id=%s,age=%s,username='%s',password='%s',gender='%s',email='%s' where id=%s" %(id,age,username,pwd,gender,email,nid)
        #sql = "update user set age=%s,username=%s,password=%s,gender=%s,email=%s where id=%s".format(repr(age),repr(username),repr(pwd),repr(gender),repr(email),repr(nid))
        print(sql)

        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return redirect('/cmdb/modelbox/')



def userdelete(request,nid):
    db = pymysql.connect("192.168.100.198", "django", "123456", "django")
    cursor = db.cursor()
    sql = "delete from user where id=%s" %nid
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    return redirect('/cmdb/modelbox')




def business(request):
    v1 = models.Business.objects.all()
    #返回对象
    v2 = models.Business.objects.all().values('id','caption')
    #返回字典
    v3 = models.Business.objects.all().values_list('id','caption')
    #返回元组，按索引取数据
    return render(request, 'index.html', {'v1':v1})

def host(request):
    v1 = models.Host.objects.filter(nid__gt=0)
    for row in v1:
        print(row.nid, row.hostname, row.ip, row.port, row.b.caption)

    v2 = models.Host.objects.filter(nid__gt=0).values('nid', 'hostname', 'ip', 'port', 'b__caption', 'b_id')
    for row in v2:
        print(row['nid'],row['hostname'],row['b__caption'])

    v3 = models.Host.objects.filter(nid__gt=0).values_list('nid', 'hostname', 'ip', 'port', 'b__caption', 'b_id')
    for row in v3:
        print(row[0], row[1], row[4])

    return HttpResponse('host')


# def app(request):
#     if request.method == "GET":
#         app_list = models.Appliaction.objects.all()
#         # for row in app_list:
#         #     print(row.name,row.r.all())
#         host_list = models.Host.objects.all()
#         return render(request, 'app.html', {'app_list': app_list, 'host_list':host_list})
#     elif request.method == "POST":
#         print(request)
#         app_name = request.POST.get('app_name')
#         host_list = request.POST.getlist('host_list')
#         #print(app_name,host_list)
#
#         obj = models.Appliaction.objects.create(name=app_name)
#         obj.r.add(*host_list)
#         return redirect('/cmdb/app')

def ajax_add_app(request):
    ret = {'status': True, 'error': None, 'data': None}
    print(request.POST.get('app_name'))
    print(request.POST.getlist('hostlist'))
    return HttpResponse(json.dumps(ret))


################################
from utils import pagination

LIST = []
for i in range(99):
    LIST.append(i)


def user_list(request):
    current_page = request.GET.get('p', 1)
    current_page = int(current_page)

    val = request.COOKIES.get('per_page_count', 10)
    val = int(val)

    page_obj = pagination.Page(current_page, len(LIST), val)

    data = LIST[page_obj.start:page_obj.end]

    page_str = page_obj.page_str("/cmdb/user_list/")

    return render(request, 'user_list.html', {'li': data, 'page_str': page_str})
###################################

# def index(request):
#
#     v = request.COOKIES.get('username_cookie')
#     if not v:
#         return redirect('/cmdb/login/')
#     return render(request,'index.html', {'current_user': v})


#装饰器应用
def auth(func):
    def inner(request,*args,**kwargs):
        v = request.COOKIES.get('username_cookie')
        if not v:
            return redirect('/cmdb/login/')
        return func(request,*args,**kwargs)
    return inner

#装饰器调用
@auth
def app(request):
    if request.method == "GET":
        app_list = models.Appliaction.objects.all()
        # for row in app_list:
        #     print(row.name,row.r.all())
        host_list = models.Host.objects.all()
        return render(request, 'app.html', {'app_list': app_list, 'host_list':host_list})
    elif request.method == "POST":
        print(request)
        app_name = request.POST.get('app_name')
        host_list = request.POST.getlist('host_list')
        #print(app_name,host_list)

        obj = models.Appliaction.objects.create(name=app_name)
        obj.r.add(*host_list)
        return redirect('/cmdb/app')