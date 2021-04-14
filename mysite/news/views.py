from django.shortcuts import render
from django.http import HttpResponse
from .models import News
from .forms import TaskForm


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'news/index.html', context)


def admin(request):
    return render(request, 'news/admin')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'form is error'

    form = TaskForm()
    context = {
        'form': form,
        'error': error,
        'title': 'Добавить статью'
    }
    return render(request, 'news/create.html', context)
