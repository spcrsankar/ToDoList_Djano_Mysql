from django import forms
from .models import Users, ToDos

class UsersRegistrationForm(forms.ModelForm):
  class Meta:
    model = Users
    fields = "__all__"
    widgets = {
      "name": forms.TextInput(attrs={"class": "name"}),
      "email": forms.TextInput(attrs={"class": "email"}),
      "password": forms.PasswordInput(attrs={"class": "password"}),
    }

class ToDoForm(forms.ModelForm):
  class Meta:
    model = ToDos
    # fields = "__all__"
    fields = [ 'title', 'description', 'status', 'due_date']
    widgets = {
      "user": forms.Select(attrs={"class": "user"}),
      "title": forms.TextInput(attrs={"class": "title","placeholder":"Enter Title"}),
      "description": forms.TextInput(attrs={"class": "description","placeholder":"Enter Description"}),
      "status": forms.Select(attrs={"class": "status"}),
      "due_date": forms.DateInput(attrs={"class": "due_date","placeholder":"YYYY-MM-DD"}),
    }
    