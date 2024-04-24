from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import User, Task
from .forms import UserForm, TaskForm
import pandas as pd


def index(request):
    return render(request, 'index.html') 

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})
    

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tasks')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def list_users(request):
    users = User.objects.all()
    paginator = Paginator(users, 50) 
    page = request.GET.get('page')
    users_page = paginator.get_page(page)
    return render(request, 'list_users.html', {'users': users_page})

def list_tasks(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 50)
    page = request.GET.get('page')
    tasks_page = paginator.get_page(page)
    return render(request, 'list_tasks.html', {'tasks': tasks_page})

def export_to_excel(request):
    users = User.objects.all()
    tasks = Task.objects.all()

    users_df = pd.DataFrame(users.values())
    tasks_df = pd.DataFrame(tasks.values())

    writer = pd.ExcelWriter('user_tasks.xlsx', engine='xlsxwriter')

    users_df.to_excel(writer, sheet_name='Users', index=False)
    tasks_df.to_excel(writer, sheet_name='Tasks', index=False)

    writer.close()

    with open('user_tasks.xlsx', 'rb') as excel_file:
        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=user_tasks.xlsx'
        return response
