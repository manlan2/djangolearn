from django.shortcuts import render
from django.contrib.auth.models import User
from models import employ

# Create your views here.
def hello(request):
	# user_list = User.objects.all()


	user_list = employ.objects.all()
	return render(request, 'table.html', {'userArray':user_list})

def hi(request):
    emp = employ()
    emp.name = 'binbinbin'
    emp.save()
    return render(request, '404.html')

# def helloa(request):
# 	user_list = User.objects.all()
# 	return render(request, 'table2.html', {'userArray':user_list})