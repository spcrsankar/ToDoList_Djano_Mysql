from django.shortcuts import render, get_object_or_404
from .models import Users, ToDos
from .forms import UsersRegistrationForm, ToDoForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
# Create your views here.


class UserRegistration(CreateView):
  model = Users
  form_class = UsersRegistrationForm
  template_name = "ToDoApp/user_signup.html"
  success_url = "/user_login"


def userLogin(request):
  if request.method == "POST":
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = Users.objects.get(email=email, password=password)
    print(user)
    if user:
      request.session['username'] = user.name
      request.session['email'] = user.email
      request.session['id'] = user.id
      return redirect("todo_list")
    else:
      return render(request, "ToDoApp/user_login.html",{"msg":"invalid username or password"})
  else:
    return render(request, "ToDoApp/user_login.html")


def userLogout(request):
  try:
    del request.session['username']
  except:
    pass
  return redirect("/user_login")

def todo_list(request):
    if request.session.has_key('username'):
      id = request.session['id']
      todos = ToDos.objects.filter(user_id=id)
      return render(request, 'todoapp/todo_list.html', {'todos': todos})
    else:
      return redirect("/user_login")

def todo_create(request):
    if request.session.has_key('username'):

      if request.method == 'POST':
        user = Users.objects.get(id=request.session['id'])
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user  # Assuming you're using request.user for authentication
            todo.save()
            return redirect('todo_list')
      else:
          form = ToDoForm()
      return render(request, 'todoapp/todo_form.html', {'form': form})
    else:
      return redirect("/user_login")
def todo_update(request, pk):
    if request.session.has_key('username'):
      todo = get_object_or_404(ToDos, pk=pk)
      if request.method == 'POST':
          form = ToDoForm(request.POST, instance=todo)
          if form.is_valid():
              form.save()
              return redirect('todo_list')
      else:
          form = ToDoForm(instance=todo)
      return render(request, 'todoapp/todo_form.html', {'form': form})
    else:
      return redirect("/user_login")

def todo_delete(request, pk):
    if request.session.has_key('username'):
      todo = get_object_or_404(ToDos, pk=pk)
      if request.method == 'POST':
          todo.delete()
          return redirect('todo_list')
      return render(request, 'todoapp/todo_confirm_delete.html', {'todo': todo})
    else:
      return redirect("/user_login")