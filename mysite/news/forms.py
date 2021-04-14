from .models import News
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = News
        fields = ["title", "content"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form__title',
                'placeholder': 'Название статьи'
            }),
            "content": Textarea(attrs={
                'class': 'form__text',
                'placeholder': 'Введите текст'
            }),
        }
