from flask import Flask, request, jsonify
import base64
import os

app = Flask(__name__)


@app.route('/string_to_binary', methods=['GET', 'POST'])
def convert_string_to_binary():
    try:
        # Get the string data from the request JSON
        data = request.get_json()
        input_string = data.get('string')

        if not input_string:
            return jsonify({'error': 'Missing string data in request JSON'}), 400

        # Convert the input string to binary data as bytes
        binary_data = input_string.encode('utf-8')

        # Encode the binary data as base64
        base64_encoded_binary = base64.b64encode(binary_data).decode('utf-8')

        # Prepare the response JSON object
        response_data = {
            'binary': base64_encoded_binary
        }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/binary_to_string', methods=['GET', 'POST'])
def convert_binary_to_string():
    try:
        # Get the binary data from the request JSON
        data = request.get_json()
        binary_data = data.get('binary')

        if not binary_data:
            return jsonify({'error': 'Missing binary data in request JSON'}), 400

        # Decode the base64-encoded binary data to bytes
        binary_bytes = base64.b64decode(binary_data)

        # Convert the binary data to a human-readable string
        converted_string = binary_bytes.decode('utf-8')

        # Prepare the response JSON object
        response_data = {
            'string': converted_string
        }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=True)
