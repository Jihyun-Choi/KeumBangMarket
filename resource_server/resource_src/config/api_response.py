from rest_framework.response import Response
from rest_framework import status


def api_response(success=True, message="Success", data=None, errors=None, status_code=status.HTTP_200_OK):
    response = {
        "success": success,
        "status": status_code,
        "message": message,
        "data": data if data is not None else [],
    }

    if errors:
        response["errors"] = errors

    return Response(response, status=status_code)
