from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm, PostForm
from django.contrib.auth.decorators import login_required


def Home_Bage(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'topics.html', {'board': board})


@login_required
def new_topic(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    user = User.objects.first()
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = request.user
            topic.save()

            post = Post.objects.create(
                message = form.cleaned_data.get('message'),
                created_by = request.user,
                topic = topic,
            )
            return redirect('new_topic', board_id = board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})


def topic_posts(request, board_id, topic_id):
    topic = get_object_or_404(Topic, board__pk=board_id, pk=topic_id)
    return render(request, 'topic_posts.html', {'topic': topic})


@login_required
def reply_topic(request, board_id, topic_id):
    topic = get_object_or_404(Topic, board__pk=board_id, pk=topic_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()

            return redirect('topic_posts.html', board_id=board_id, topic_id=topic_id)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic ,'form': form})

# old Funcation
# def new_topic(reqest, board_id):
#     board = get_object_or_404(Board, pk=board_id)
#     if reqest.method == 'POST':
#         subject = reqest.POST['subject']
#         message = reqest.POST['message']
#         user = User.objects.first()

#         topic = Topic.objects.create(
#             subject = subject,
#             board = board,
#             created_by = user
#         )
#         post = Post.objects.create(
#             message = message,
#             topic = topic,
#             created_by = user
#         )
#         return redirect('board_topics', board_id = board.pk)
#     return render(reqest, 'new_topic.html', {'board': board})


# Video 9
# def Home_Bage(reqest):
#     boards = Board.objects.all()
#     boards_names = []
#     for board in boards:
#         boards_names.append(board.name)
#     respones_html = '<br><br>'.join(boards_names)
#     return HttpResponse(respones_html)