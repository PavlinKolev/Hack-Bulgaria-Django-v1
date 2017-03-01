from django.http import HttpResponse
import json
from calculator.helpers import factorial


def add(request, a, b):
    res = int(a) + int(b)
    format = request.GET.get('format', '')
    if format == 'json':
        data = {
            "result": res
        }
        response = HttpResponse(json.dumps(data, indent=4))
        response['Content-Type'] = 'application/json'
        return response
    return HttpResponse(res)


def multiply(request, a, b):
    res = int(a) * int(b)
    format = request.GET.get('format', '')
    if format == 'json':
        data = {
            "result": res
        }
        response = HttpResponse(json.dumps(data, indent=4))
        response['Content-Type'] = 'application/json'
        return response
    return HttpResponse(res)


def power(request, a, b):
    res = int(a) ** int(b)
    format = request.GET.get('format', '')
    if format == 'json':
        data = {
            "result": res
        }
        response = HttpResponse(json.dumps(data, indent=4))
        response['Content-Type'] = 'application/json'
        return response
    return HttpResponse(res)


def fact(request, n):
    res = factorial(int(n))
    format = request.GET.get('format', '')
    if format == 'json':
        data = {
            "result": res
        }
        response = HttpResponse(json.dumps(data, indent=4))
        response['Content-Type'] = 'application/json'
        return response
    return HttpResponse(res)
