from django.contrib import admin
from .models import Board, Post, Topic
from .forms import NewTopicForm

admin.site.register(Board)
admin.site.register(Post)
admin.site.register(Topic)
