from django.shortcuts import render
from django.shortcuts import HttpResponse

from django.shortcuts import redirect

from app02 import models
# Create your views here.


def newlogin(request):
    error_msg = ''
    if request.method == "POST":
        # 获取用户通过post提交过来的数据
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        if user == 'admin' and pwd == '123456zxc':
            # return redirect('http://baidu.com')
            # return redirect('/home')
            return redirect('/modelbox')
        else:
            error_msg = "用户名密码错误"
    return render(request, 'login.html', {'error_msg': error_msg})


def orm(request):
    #增删改查
    #增加数据
    #models.UserInfo.objects.create(username='root',password='123')
    # obj = models.UserInfo(username='ass',password='123')
    # obj.save()
    #-------------------------------------

    #查数据
    #result = models.UserInfo.objects.all()
    #result = models.UserInfo.objects.filter(username='root')
    #返回QuerySet类型
    # for row in result:
    #     print(row.id,row.username,row.password)
    # print(result)
    #------------------------------------

    #删除
    #models.UserInfo.objects.filter(id=4).delete()
    # ------------------------------------

    #改 更新
    #models.UserInfo.objects.all().update(password='6669999')
    models.UserInfo.objects.filter(id=4).update(password=33333)

    return HttpResponse('orm')