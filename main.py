from flask import Flask, jsonify, request
import requests

from werkzeug.datastructures import MultiDict

app = Flask(__name__)


# Add "self" parameter when working with Google Cloud.
@app.route('/canvas_api', methods=['GET'])
def canvas_api(self):
    # Allows GET requests from any origin with the Content-Type
    # header and caches preflight response for an 3600s
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': '*',
        'Access-Control-Allow-Headers': '*'
    }

    if request.method == 'OPTIONS':
        return ('', 204, headers)

    try:
        access_token = request.headers.get('X-Canvas-Authorization')

        if access_token is not None:
            headers_canvas = {
                'Authorization': access_token,
            }

            query_params = request.args
            endpoint = query_params.get('endpoint')
            array_params = MultiDict()

            for k in query_params.keys():
                app.logger.error("value: " + k + ' - ' + str(k != "endpoint"))
                if k != 'endpoint':
                    array_params.add(k, query_params.get(k))

            url = requests.get(
                'https://fhict.instructure.com/api/v1/' + endpoint,
                params=array_params,
                headers=headers_canvas
            )

            return jsonify({
                "url": url.url,
                "message1": url.json()
            }), 200, headers
        else:
            return jsonify({
                "message": "Access Token incorrect"
            }), 200, headers
    except Exception as e:
        app.logger.error(e)
        return jsonify({
            "message": "Unable to call API"
        }), 200, headers
