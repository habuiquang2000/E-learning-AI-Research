from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponse
# from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
User = get_user_model()


class Profile(LoginRequiredMixin, View):
    login_url = "/signin/"

    def get(self, req):
        return render(req, "user/auth/profile.html")


class LogoutView(LoginRequiredMixin, View):
    login_url = "/signin/"

    def get(self, req):
        logout(req)
        return redirect("home")


class SignUpView(View):
    def get(self, request):
        if request.user.id:
            return redirect("home")

        return render(request, "user/auth/signup.html")

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["user_id"]
        email = request.POST["email"]
        pass_word1 = request.POST["pass_word1"]
        pass_word2 = request.POST["pass_word2"]

        if pass_word1 == pass_word2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "tên đăng nhập")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email đã tồn tại")
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=pass_word1,
                    email=email,
                )
                
                user.save()
                messages.info(request, "đăng ký thành công")
        else:
            messages.info(request, "mật khẩu không khớp")
        return redirect("sign_up")


class SignInView(View):
    def get(self, request):
        if request.user.id:
            return redirect("home")
        return render(request, "user/auth/login.html", )

    def post(self, request):
        user_id = request.POST.get("user_id")
        pass_word = request.POST.get("pass_word")
        check = authenticate(username=user_id, password=pass_word)
        print(user_id)
        print(pass_word)
        if check is None:
            messages.info(request, "Mã sinh viên hoặc mật khẩu đã sai")
            return redirect("sign_in")
        login(request, check)
        return redirect("home")
