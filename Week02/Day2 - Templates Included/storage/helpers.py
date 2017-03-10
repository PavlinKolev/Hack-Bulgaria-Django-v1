from api_storage.models import User, Data


def add_key_value_to_user(user, key, value):
    try:
        data = user.data_set.get(key=key)
        data.value = value
    except Data.DoesNotExist:
        data = Data.objects.create(key=key, value=value, user=user)
    finally:
        data.save()
