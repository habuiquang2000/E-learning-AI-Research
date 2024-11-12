from django.shortcuts import render

# Create your views here.


def handler404(req, exception):
    return render(req, "error/404.html")


def handler500(req):
    return render(req, "error/500.html")
