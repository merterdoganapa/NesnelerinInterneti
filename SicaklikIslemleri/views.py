from django.shortcuts import render
from mailGonderme import mailGonder

# Create your views here.


def index(request):
    if request.method == "POST":
        email = request.POST.get("email")
        mailGonder(email)
        return render(request,"info.html")
    return render(request,"index.html")

    
    