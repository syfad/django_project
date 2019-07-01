from django.shortcuts import render
from django.shortcuts import HttpResponse

from django.shortcuts import redirect

from app02 import models
# Create your views here.


def newlogin(request):
    error_msg = ''
    #基于mysql ORM实现用户登录
    if request.method == "GET":
        return render(request,'new_login.html')
    elif request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pwd')

        obj = models.UserInfo.objects.filter(username=u,password=p).first()
        if obj:
            return redirect('/monitor/index/')
        else:
            return render(request, 'new_login.html')

        #return render(request, 'new_login.html', {'error_msg': error_msg})



def orm(request):
    #增删改查示例
    #增加数据
    #models.UserInfo.objects.create(username='root',password='123')
    # obj = models.UserInfo(username='ass',password='123')
    # obj.save()
    #-------------------------------------

    #查数据
    # result = models.UserInfo.objects.all()
    # # result = models.UserInfo.objects.filter(username='root')
    # # #返回QuerySet类型
    # for row in result:
    #     print(row.id,row.username,row.password)
    # print(result)
    #------------------------------------

    #删除
    #models.UserInfo.objects.filter(id=4).delete()
    # ------------------------------------

    #改 更新
    #models.UserInfo.objects.all().update(password='6669999')
    #models.UserInfo.objects.filter(id=4).update(password=33333)


    #外键 一对多
    models.UserInfo.objects.create(
        username='admin123',
        password='123456',
        email='admin@123.com',
        #user_group = models.UserGroup.objects.filter(id=1).first()
        user_group_id= 1
    )


    return HttpResponse('orm')


def index(request):
    return render(request, 'index.html')

def user_info(request):
    if request.method == "GET":
        user_list = models.UserInfo.objects.all()
        group_list = models.UserGroup.objects.all()
        return render(request, 'user_info.html', {'user_list': user_list}, {'group_list': group_list})

    elif request.method == "POST":
        u = request.POST.get("username")
        p = request.POST.get("password")
        models.UserInfo.objects.create(username=u,password=p)
        user_list = models.UserInfo.objects.all()
        return render(request, 'user_info.html', {'user_list': user_list})

def user_del(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/monitor/user_info/')

def user_edit(request, nid):
    if request.method == "GET":
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'user_edit.html', {'obj': obj})
    elif request.method == "POST":
        nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        # e = request.POST.get('email')
        models.UserInfo.objects.filter(id=nid).update(username=u, password=p,)
        return redirect('/monitor/user_info/')


def user_detail(request, nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    return render(request, 'user_detail.html', {'obj': obj})
