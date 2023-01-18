from django.forms import ModelForm
form .models import Todo

class TodoForm(ModelForm)
    class Meta:
        model = Todo
        fields = '__all__'
