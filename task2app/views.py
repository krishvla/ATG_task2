from django.shortcuts import render,redirect
from task2app.models import users,articles
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from werkzeug.utils import secure_filename
import os
# Creatr views here
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "../static/css/users")

def home(request):
    # return redirect(frequency)
    return render(request,"home.html")

def reg(request):
    # return redirect(frequency)
    if request.method == 'POST':
        usern = request.POST['username']
        passw = request.POST['password']
        set_user = users(username=usern,password=passw)
        set_user.save()
        request.session['user'] = usern
        return redirect(dashboard)
    return render(request,"reg.html")

def login(request):    # return redirect(frequency)
    if request.method == 'POST':
        usern = request.POST['username']
        passw = request.POST['password']
        if users.objects.filter(username=usern).exists():
            data = users.objects.get(username=usern)
            if(data.password == passw):
                request.session['user'] = usern
                return redirect(dashboard)
            else:
                return render(request,"login.html",{"error": "Password Mismatch"})
        else:
            return render(request,"login.html",{"error": "User Not Exsists"})


    return render(request,"login.html")

def check(request):
    if request.method == 'POST':
        name = request.POST['name']
        if users.objects.filter(username=name).exists():
            return HttpResponse('exsists')
        else:
            return HttpResponse('no')

def dashboard(request):
    if request.method == 'POST':
        aid = request.POST['aid']
        cd = articles.objects.get(id=aid)
        if cd.publish == 'private':
            articles.objects.filter(id=aid).update(publish='public')
            return redirect(dashboard)
        elif cd.publish == 'public':
            articles.objects.filter(id=aid).update(publish='private')
            return redirect(dashboard)


    if(request.session.get('user')):
        uname=request.session['user']
        data = articles.objects.filter(username=uname)
        return render(request,"dash.html",{"data":data})
    else:
        return redirect(login)

def create(request):
    if request.method == 'POST'and request.FILES['myfile']:
        usern = request.session['user']
        dis = request.POST['description']
        articlename = request.POST['name']
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        filepath = uploaded_file_url
        print(uploaded_file_url)
        pub = request.POST['pub']
        set_article = articles(article_name=articlename,content=dis,username=usern,image=filepath,publish=pub)
        set_article.save()
        return render(request,'create.html',{"msg":"Created Successfully"})
    if(request.session.get('user')):
        return render(request,"create.html")
    else:
        return render(request,'login.html',{"error": "Please Login"})

def search(request):
    if(request.session.get('user')):
        data = articles.objects.filter(publish='public')
        return render(request,"search.html",{"data":data})

def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return redirect(login)