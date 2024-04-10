from django.shortcuts import render
from django.http import HttpResponse
import json
def test_function(request):
    return HttpResponse(request,'<h3>Регистрация</h3>')
def func(request):
    return render(request,'main/registration.html')
def login(request):
    return render(request, 'main/login.html')
def new_user(new_user):
    with open("list_of_users.json", "r") as file:
        existing_data = json.load(file)
    existing_data.append(new_user)

    with open("list_of_users.json", "w") as file:
        json.dump(existing_data, file, indent=4)
def profile_view():
    return HttpResponse("<h3>ничего</h3>>")

