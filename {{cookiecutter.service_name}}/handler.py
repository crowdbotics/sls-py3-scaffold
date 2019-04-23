import json


def hello(event, context):
    body = {
        "message": "Congratulations! You just released your first serverless function - {{cookiecutter.service_name}} - with Crowdbotics! Reward yourself! Grab a cup of coffee!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
