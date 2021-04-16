from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic import UpdateView
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
    print(request)
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


def delete(request, id):
    try:
        news = News.objects.get(id=id)
        news.delete()
        return HttpResponseRedirect('/')
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Article not found</h2>")


def edit(request, id):
    try:
        news = News.objects.get(id=id)
        context = {
            'news': news
        }
        if request.method == 'POST':
            form = TaskForm(request.POST, instance=news)
            form.save()
            return redirect('home')
        else:
            return render(request, 'news/edit.html', context)
    except News.DoesNotExist:
        return HttpResponseNotFound("<h2>Article not found</h2>")
