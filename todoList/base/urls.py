from django.urls import path

from .views import TaskCreate, TaskDetail, TaskList, TaskUpdate, TaskDelete, Login, Registration

from django.contrib.auth.views import LogoutView

urlpatterns=[   
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Registration.as_view(), name='register-page'),

    path('',TaskList.as_view(), name='task-list'),
    path('task-detail/<int:pk>',TaskDetail.as_view(), name='task-detail'),
    path('task-create/',TaskCreate.as_view(), name='task-create'),
    path('task-upadate/<int:pk>',TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>',TaskDelete.as_view(), name='task-delete'),

]
