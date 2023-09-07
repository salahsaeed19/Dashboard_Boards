from django import forms
from .models import Topic, Post, Board


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        max_length=4000,
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your message here'}),
        help_text='Max length: 4000 characters',
        label='Message'
    )
    
    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message']