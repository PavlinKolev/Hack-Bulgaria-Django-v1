import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from storage.helpers import new_user_identifier, get_user_file_name


def create_user(request):
    if request.method == "GET":
        data = {"identifier": new_user_identifier()}
        response = JsonResponse(data)
        return response
    return JsonResponse({"Error": "Unsupported request method."}, status=404)


@csrf_exempt
def set_user_data(request, user_id):
    if request.method == "POST":
        try:
            user_file = get_user_file_name(user_id)
            user_data = json.loads(request.body.decode('utf-8'))
            with open(user_file, 'w') as f:
                f.truncate()
                f.writelines(json.dumps(user_data))
            return JsonResponse(user_data, status=201)
        except ValueError:
            return JsonResponse({"Error": "Key not found"}, status=404)
    return JsonResponse({"Error": "Unsupported request method."}, status=404)


@csrf_exempt
def user_data_by_key(request, user_id, key):
    try:
        user_file = get_user_file_name(user_id)
        with open(user_file, 'r') as f:
            user_data = json.load(f)
            if user_data['key'] != key:
                raise KeyError("Wrong key for user.")
    except (ValueError, KeyError):
        return JsonResponse({"Error": "Key not found"}, status=404)
    else:
        if request.method == "GET":
            return JsonResponse({"value": user_data['value']})
        elif request.method == "DELETE":
            with open(user_file, 'w') as f:
                f.truncate()
                f.writelines(json.dumps({}))
            return JsonResponse({"Request status": "Accepted"}, status=202)
        return JsonResponse({"Error": "Unsupported request method."}, status=404)
