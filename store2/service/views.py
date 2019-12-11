from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Model
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm

def example_view(request):
    return render(request, 'base.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    form = UserCreationForm()
    return render(request, 'registration/signup.html',{
    'form':form
    })


class ServiceModel(ListView):
    ''' Список услуг по категориям'''
    model = Model
    context_object_name = 'service_category'
    template_name = 'service_category.html'

    def get_queryset(self):
        return Model.objects.filter(category__slug = self.kwargs.get('slug'))


class ServiceModelView(DetailView):
    model = Model
    context_object_name = 'service_model_view'
    template_name = 'service_model.html'

    def get_queryset(self):
        return Model.objects.filter(category__slug = self.kwargs.get('category'), slug = self.kwargs.get('slug'))
