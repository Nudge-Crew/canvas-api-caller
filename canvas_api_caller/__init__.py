import requests
import json
import os


def call(access_token, params):
    if access_token and params.get('endpoint') is not None:
        try:
            headers = {
                'Authorization': access_token
            }

            endpoint = params.get('endpoint')
            query_params = []

            for p in params.keys():
                if p != 'endpoint':
                    query_params.append([p, params.get(p)])

            url = requests.get(
                os.environ.get('CANVAS_BASE_URL') + endpoint,
                params=query_params,
                headers=headers
            )

            return json.dumps({
                "code": url.status_code,
                "url": url.url,
                "message": url.json()
            })
        except Exception as e:
            return json.dumps({
                "code": 500,
                "message": e,
                "url": None
            })
    else:
        if access_token is None:
            return json.dumps({
                "message": "Access Token not found",
                "code": 401,
                "url": None
            })
        elif params.get('endpoint') is None:
            return json.dumps({
                "message": "Canvas Endpoint not specified",
                "code": 404,
                "url": None
            })
        else:
            return json.dumps({
                "message": "Unable to call Canvas API",
                "code": 500,
                "url": None
            })
