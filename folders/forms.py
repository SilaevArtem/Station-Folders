from fileinput import FileInput
from django.forms import ModelForm, TextInput, Textarea, DateInput
from .models import Folders


class FoldersForm(ModelForm):
    class Meta:
        model = Folders
        fields = ['title', 'descrip', 'datecomplited', 'file']
        widgets = {'title': TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Введите Название Папки Заглавными Буквами'
        }),
        'descrip': Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введите Краткое Описание' 
        }),
        'datecomplited': DateInput(attrs={
            'class': 'col-3',
            'placeholder': 'Введите Дату'})
            }

