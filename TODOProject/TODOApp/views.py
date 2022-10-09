import datetime

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from TODOApp.models import Todo


class MyTodo(View):
    def get(self,request):
        todo_list = Todo.objects.all()
        today = datetime.date.today()
        context = {'todo_list':todo_list,'today':today}
        return render(request,'todoList.html',context)

    def post(self,request):
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        Todo.objects.create(
            completeAt=date,
            desc=desc
        )
        messages.success(request,'Todo created successfully')
        return HttpResponse('todo created')

    @staticmethod
    def delete_todo(request):
        todo_id = request.GET.get('todo')
        Todo.objects.get(
            id=todo_id
        ).delete()
        messages.error(request,'Todo deleted successfully')
        return HttpResponse('todo created')

    @staticmethod
    def complete_todo(request):
        todo_id = request.GET.get('todo')
        todo_data = Todo.objects.get(
            id=todo_id
        )
        todo_data.isCompleted = True
        todo_data.taskCompletedDate = datetime.date.today()
        todo_data.save()
        messages.success(request, 'Todo completed successfully')
        return HttpResponse('todo created')

    @staticmethod
    def todo_filter(request):
        filter_type = request.GET.get('filter_type')
        flag = True
        if filter_type == 'pending':
            flag = False
        elif filter_type == 'all_task':
            todo_list = Todo.objects.all().order_by('isCompleted')
            context = {'todo_list': todo_list,'all':filter_type}
            return render(request, 'filterTodo.html', context)

        todo_list = Todo.objects.filter(isCompleted=flag)
        context = {'todo_list':todo_list}
        return render(request,'filterTodo.html',context)