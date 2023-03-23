from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('login_handle', views.login_handle, name="login_handle"),
    path('signup_handle', views.signup_handle, name="signup_handle"),
    path('logout_handle', views.logout_handle, name="logout_handle"),
    path('todo', views.todo, name="todo"),
    path('task_done_btn_handle', views.task_done_btn_handle, name="task_done_btn_handle"),
    path('task_to_be_done_btn_handle', views.task_to_be_done_btn_handle, name="task_to_be_done_btn_handle"),
    path('new_task', views.new_task, name="new_task"),
    path('new_task_handle', views.new_task_handle, name="new_task_handle"),
    path('delete_task', views.delete_task, name="delete_task")
]
