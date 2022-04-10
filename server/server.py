from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
'''
General Header: This type of headers applied on Request and Response headers both but with
 out affecting the database body. Request Header: This type of headers contains information
  about the fetched request by the client. Response Header: 
This type of headers contains the location of the source that has been requested by the client.
'''

if __name__=='__main__':
    print("Starting Python Flask Server For Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(debug=True)