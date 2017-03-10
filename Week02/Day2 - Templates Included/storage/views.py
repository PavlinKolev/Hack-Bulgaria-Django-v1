from django.shortcuts import render, redirect
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from api_storage.models import User, Data
from storage.helpers import add_key_value_to_user


def index(request):
    users = User.objects.all()
    user_count = User.objects.count()
    key_count = 0
    key_hist = {}
    for user in User.objects.all():
        key_count += user.data_set.count()
        for data in user.data_set.all():
            if data.key in key_hist.keys():
                key_hist[data.key] += 1
            else:
                key_hist[data.key] = 1

    return render(request, 'index.html', locals())


def user_detail(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user_data = user.data_set.all()
        return render(request, 'user_detail.html', locals())
    except (User.DoesNotExist, ValueError):
        raise Http404("No user with this id.")


@csrf_exempt
def add_key(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except (User.DoesNotExist, ValueError):
        raise Http404("No user with this id.")
    else:
        if request.method == "POST":
            key = request.POST.get('key')
            value = request.POST.get('value')
            add_key_value_to_user(user, key, value)
            return redirect('storage:user_detail', user_id=user.id)
        return render(request, 'add_key.html', locals())










        #
