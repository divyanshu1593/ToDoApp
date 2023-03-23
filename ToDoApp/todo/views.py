from django.shortcuts import render, redirect
from .models import Person, Tasks

# Create your views here.

#global variables
nav = '''
    <form action="login">
        <input type="submit" value="login" id="login_btn">
    </form>
'''

add_task = '''
            <form action="new_task">
                <input type="submit" value="add new task" id="add_btn">
            </form>
    '''

isLogin = False
user = ""

def new_task(request):
    global add_task

    add_task = '''
            <form action="new_task_handle" id="adding_task">
                <input type="text" name="newTask">
                <input type="submit" value"add task">
            </form>
    '''

    return redirect(todo)

def new_task_handle(request):
    global user, add_task
    text = request.GET['newTask']
    obj = Tasks(desc=text, belongsTo=Person.objects.get(username=user))
    obj.save()

    add_task = '''
            <form action="new_task">
                <input type="submit" value="add new task" id="add_btn">
            </form>
    '''

    return redirect(todo)

def task_done_btn_handle(request):
    p = int(request.GET['hd'])
    obj = Tasks.objects.get(pk=p)
    obj.isDone = False
    obj.save()
    return redirect(todo)

def task_to_be_done_btn_handle(request):
    p = int(request.GET['hd'])
    obj = Tasks.objects.get(pk=p)
    obj.isDone = True
    obj.save()
    return redirect(todo)

def delete_task(request):
    p = int(request.GET['hd'])
    obj = Tasks.objects.get(pk=p)
    obj.delete()
    return redirect(todo)

def todo(request):
    global add_task
    try:
        obj = Person.objects.get(username=user)
    except:
        return redirect(home)
    task_done = ""
    task_to_be_done = ""

    # getting the all the task of the user
    t = list(obj.tasks_set.all())
    for task in t:
        if task.isDone:
            task_done += '''
                <div class="task_done_">
                    <form action="task_done_btn_handle" style="display:inline">
                            <input type="hidden" value="{}" name="hd">
                        {}  <input type="submit" value="" class="task_done_btn">
                    </form>
                    <form action="delete_task" style="display:inline">
                            <input type="hidden" value="{}" name="hd">
                            <input type="submit" value="" class="delete_task_btn">
                    </form>
                    <br>
                </div>
            '''.format(task.pk, task.desc, task.pk)
        else:
            task_to_be_done += '''
                <div class="task_to_be_done_"> 
                    <form action="task_to_be_done_btn_handle" style="display:inline">
                            <input type="hidden" value="{}" name="hd">
                        {}  <input type="submit" value="" class="task_to_be_done_btn">
                    </form>
                    <form action="delete_task" style="display:inline">
                            <input type="hidden" value="{}" name="hd">
                            <input type="submit" value="" class="delete_task_btn">
                    </form>
                    <br>
                </div>
            '''.format(task.pk, task.desc, task.pk)

    return render(request, 'todo.html', {'add_task':add_task,'task_to_be_done':task_to_be_done,'task_done':task_done,'name':obj.name})

def login(request):
    return render(request, 'login.html')

def login_handle(request):
    global user, isLogin
    usname = request.POST['username']
    pswd = request.POST['password']
    try:
        obj = Person.objects.get(username=usname)
        if obj.password == pswd:
            user = usname
            isLogin = True
            return redirect(home)
        return redirect(login)
    except:
        return redirect(login)

def signup_handle(request):
    nm = request.POST['name']
    usname = request.POST['username']
    pswd = request.POST['password']
    try:
        obj = Person.objects.get(username=usname)
        return redirect(signup)
    except:
        obj = Person()
        obj.name = nm
        obj.username = usname
        obj.password = pswd
        obj.save()
        return redirect(home)

def signup(request):
    return render(request, 'signup.html')

def logout_handle(request):
    global user, isLogin
    user = ""
    isLogin = False
    return redirect(home)

def home(request):
    global nav
    if isLogin:
        nav = '''
            <form action="logout_handle">
                <input type="submit" value="logout" id="logout_btn">
            </form>
            <form action="todo">
                <input type="submit" value="todo" id="todo_btn">
            </form>
        '''
    else:
        nav = '''
            <form action="login">
                <input type="submit" value="login" id="login_btn">
            </form>
        '''
    return render(request, 'home.html', {'nav':nav})