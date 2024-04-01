from django import forms
from django.utils import timezone 
from django.forms import DateTimeInput
from .models import Task, Project
#Кастомизированный пикер даты и времени для удобства их ввода
class CustomDateTimeInput(DateTimeInput):
    def __init__(self, attrs=None, format=None):
        default_attrs = {'type': 'datetime-local'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs, format='%Y-%m-%dT%H:%M:%S')
#Форма для создания/изменения задач
class CreateTask(forms.ModelForm):
    deadline = forms.DateTimeField(label='Крайний срок*',widget=CustomDateTimeInput)
    reminder = forms.DateTimeField(label='Напоминание',widget=CustomDateTimeInput, required=False)
    class Meta:
        model = Task
        fields = ('project', 'title', 'description', 'deadline', 'reminder', 'status', 'task_user')
        labels = {
            'project': 'Проект*',
            'title': 'Задача*',
            'description': 'Описание',
            'status': 'Статус',
            'task_user': 'Пользователь*'
        }

    def __init__(self, *args, **kwargs):
        super(CreateTask, self).__init__(*args, **kwargs)
        self.fields['project'].empty_label = 'Выберите проект'
        self.fields['status'].empty_label = 'Выберите статус'
        self.fields['task_user'].empty_label = 'Выберите пользователя'
    #Устанавливаем дату создания задачи
    def save(self, commit=True):
        task = super(CreateTask, self).save(commit=False)
        if commit:
            task.created_date = timezone.now()
            task.save()
        return task
#Форма для создания/изменения проектов
class CreateProject(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name','description',)
        labels = {'name':'Название*',
                  'description':'Описание',}
    def __init__(self, *args, **kwargs):
        super(CreateProject, self).__init__(*args, **kwargs)