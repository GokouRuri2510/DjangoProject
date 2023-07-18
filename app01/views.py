from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("欢迎使用Django")

def login(request):
    print(request.POST.get("username"))
    print(request.POST.get("password"))
    return render(request, "login.html")

def get_user(request):
    list=['zhangsan','lisi']
    return render(request,'user.html', {'list':list})

