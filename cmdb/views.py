from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

import pymysql

def login(request):
    error_msg = ''
    if request.method == "POST":
        #获取用户通过post提交过来的数据
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        if user=='admin' and pwd=='123456zxc':
            #return redirect('http://baidu.com')
            #return redirect('/home')
            return redirect('/modelbox')
        else:
            error_msg = "用户名密码错误"
    return render(request, 'login.html', {'error_msg': error_msg})

def register(request):
    return render(request, 'register.html')

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
    db = pymysql.connect("192.168.100.198", "django", "123456", "django")
    #cursor = db.cursor()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select * from user")
    data = cursor.fetchall()
    #print(data)
    db.close()
    return render(request, 'modelbox.html', {'data_list': data})

#查看详细：
def detail(request, uid):
    # uid = request.GET.get("nid")
    db = pymysql.connect("192.168.100.198", "django", "123456", "django")
    #cursor = db.cursor()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select * from user where id=%s"%(uid))
    data = cursor.fetchall()
    #print(data)
    db.close()
    return render(request, 'detail.html', {'list': data})

def index(request, uid, nid):
    print(uid, nid)
    print(request.path_info)

    from django.urls import reverse
    #v = reverse('indexx', args=(90,88,))
    v = reverse('indexx', args={"nid":1, 'uid': '99'})
    print(v)
    return HttpResponse('<h1>welcome to CMDB pages</h1>')
