import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from storage.models import User, Data


def create_user(request):
    if request.method == "GET":
        new_user = User.objects.create(name="User")
        data = {"identifier": new_user.id}
        response = JsonResponse(data)
        return response
    return JsonResponse({"Error": "Unsupported request method."}, status=404)


@csrf_exempt
def set_user_data(request, user_id):
    if request.method == "POST":
        try:
            user = User.objects.get(id=user_id)
            user_data = json.loads(request.body.decode('utf-8'))
            key = user_data['key']
            value = user_data['value']
            if user.data_set.filter(key=key).count() == 1:
                user_data = user.data_set.get(key=key)
                user_data.value = value
                user_data.save()
            else:
                Data.objects.create(key=key, value=value, user=user)
            return JsonResponse(user_data, status=201)
        except Exception:
            return JsonResponse({"Error": "Key not found"}, status=404)
    return JsonResponse({"Error": "Unsupported request method."}, status=404)


@csrf_exempt
def user_data_by_key(request, user_id, key):
    try:
        user = User.objects.get(id=user_id)
        user_data = user.data_set.get(key=key)
    except Exception:
        return JsonResponse({"Error": "Key not found"}, status=404)
    else:
        if request.method == "GET":
            return JsonResponse({"value": user_data.value})
        elif request.method == "DELETE":
            user_data.delete()
            return JsonResponse({"Request status": "Accepted"}, status=202)
        return JsonResponse({"Error": "Unsupported request method."}, status=404)
