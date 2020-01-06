from flask import Flask, jsonify, request
import requests

from werkzeug.datastructures import MultiDict

app = Flask(__name__)



@app.route('/canvas_api', methods=['GET'])
def canvas_api(self):
    try:
        access_token = request.headers.get('X-Canvas-Authorization')

        if access_token is not None:
            headers = {
                'Authorization': access_token
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
                headers=headers
            )

            return jsonify({
                "url": url.url,
                "message1": url.json()
            })
        else:
            return jsonify({
                "message": "Access Token incorrect"
            })
    except Exception as e:
        app.logger.error(e)
        return "Unable to call Canvas API"
