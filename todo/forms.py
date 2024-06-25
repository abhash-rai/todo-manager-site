from django import forms
from .models import Todo
 
# create a ModelForm
class TodoForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Todo
        fields = "__all__"