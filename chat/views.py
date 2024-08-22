from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from .models import Group
from django.contrib.auth.decorators import login_required


@login_required
def home_view(request):
    groups = Group.objects.all()
    user = request.user

    context = {
        'groups': groups,
        'user': user,
    }
    return render(request, 'chat/home.html', context)


@login_required
def group_chat_view(request, uuid):
    group = get_object_or_404(Group, pk=uuid)
    if request.user not in group.members.all():
        return HttpResponseForbidden('You do not have permission to perform this action.')

    messages = group.message_set.all()
    events = group.event_set.all()

    message_and_event_list = [*messages, *events]
    sorted_message_event_list = sorted(message_and_event_list, key=lambda x: x.timestamp)

    group_members = group.members.all()
    context = {
        "message and even list": sorted_message_event_list,
        "group_members": group_members,
    }
    return render(request, 'chat/groupchat.html', context)
