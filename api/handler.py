import json

def handler(request):
    body = { "message": "Test Application For Chima" }
    return {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "application/json"
        }
    }
