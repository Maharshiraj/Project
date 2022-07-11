## >>>>> on my homepage why??

## why i couldn't update and delete even when LoginRequiredMixin, was not enforced.


from calendar import c
import imp
from inspect import stack
from locale import strcoll
from unittest.util import strclass
from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from base.models import Task 

class Login(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('task-list')  

class Registration(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task-list')

    

    # registered user directly gets logged in, doesn't go to login page 
    def form_valid(self, form):
        user = form.save()
        if user is not None:#user created successfully
            login(self.request, user)
        return super(Registration,self).form_valid(form)

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'taskslist'
    
    def get_context_data(self, **kwargs):
 
       context = super().get_context_data(**kwargs)
       print(context)
       #user=self.request.user means it will display the context data only if the intended user is logged in.
       context['taskslist'] = context['taskslist'].filter(user=self.request.user)
       context['cnt'] = context['taskslist'].filter(complete=False).count()
       
       

       search_input = self.request.GET.get('search_field') or ''
       
       if search_input:
        context['taskslist']=context['taskslist'].filter(title__startswith=search_input)
       
       context['in_search_field'] = search_input

       return context

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'taskdetail'

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('task-list')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'taskdelete'
    success_url = reverse_lazy('task-list')





