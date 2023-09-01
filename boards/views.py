from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm


def Home_Bage(reqest):
    boards = Board.objects.all()
    return render(reqest, 'home.html', {'boards': boards})


def board_topics(reqest, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(reqest, 'topics.html', {'board': board})


def new_topic(reqest, board_id):
    board = get_object_or_404(Board, pk=board_id)
    user = User.objects.first()
    if reqest.method == "POST":
        form = NewTopicForm(reqest.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = user
            topic.save()

            post = Post.objects.create(
                message = form.cleaned_data.get('message'),
                created_by = user,
                topic = topic,
            )
            return redirect('new_topic', board_id = board.pk)
    else:
        form = NewTopicForm()
    return render(reqest, 'new_topic.html', {'board': board, 'form': form})


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