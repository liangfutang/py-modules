from django.http import JsonResponse


def body(data, code: str, message: str):
    return {
        "code": code,
        "message": message,
        "data": data
    }


def success(data, code: str = '0', message: str = '操作成功'):
    return JsonResponse(body(data, code, message), safe=False)


def failure(data, code: str = '1000', message: str = '操作失败'):
    return JsonResponse(body(data, code, message), safe=False)
