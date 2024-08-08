import traceback
from django.http import JsonResponse
from django.conf import settings


def capture_error(function):
    def executor(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            response = {"error": e.__str__(), "message": "failed", "status_code": 500}
            if "UNIQUE constraint failed" in e.__str__():
                response["error"] = "Duplicate entry"
                response["status_code"] = 400
            elif "parameter is missing" in e.__str__():
                response["status_code"] = 400
            else:
                response = {
                    "error": e.__str__(),
                    "message": "failed",
                    "status_code": 500,
                }
            if settings.DEBUG:
                response["exception"] = traceback.format_exc()
            return JsonResponse(response, status=response["status_code"], safe=False)
    return executor
