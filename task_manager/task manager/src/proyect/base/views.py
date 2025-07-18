from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task


class Logueo(LoginView):
    template_name = 'base/login.html'
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tareas')


class PaginaRegistro(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tareas') ## redireccionamos a la lista de tareas

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(PaginaRegistro, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tareas')
        return super(PaginaRegistro, self).get(*args, **kwargs)

class ListaPendietes(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tareas'

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context['tareas'] = context['tareas'].filter(user=self.request.user)
        context['count'] = context['tareas'].filter(complete=False).count()

        valor_buscado = self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            context['tareas'] = context['tareas'].filter(title__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado
        return context


class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'tarea'
    # Para cambiar de nombre
    #template_name = 'base/tarea.html'


class CrearTarea(LoginRequiredMixin, CreateView):
    model = Task
    #fields = '__all__' #incorporamos a todo
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tareas')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CrearTarea, self).form_valid(form)


class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tareas')


class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')
