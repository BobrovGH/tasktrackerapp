from django.contrib import admin
from .models import Project, TaskStatus, Task

# Register your models here.
def register_models():
    models_to_register = [Project, TaskStatus, Task]
    for model in models_to_register:
        admin.site.register(model)

# Register your models here.
register_models()