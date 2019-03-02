from keras.models import Sequential, load_model
from keras.layers import Input, Dense
from keras.optimizers import SGD
from restModel import *
import tensorflow as tf

import requests, bs4
import flask
import numpy as np
import io

from flask_cors import CORS, cross_origin


from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper


app = flask.Flask(__name__)
CORS(app)
myNet = None

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

def load_model():
	# load the pre-trained Keras model (here we are using a model
	# pre-trained on ImageNet and provided by Keras, but you can
	# substitute in your own networks just as easily)
	global myNet
	myNet = NET()
	global graph
	graph = tf.get_default_graph()

@app.route("/predict", methods=["GET", "OPTIONS"])
#@crossdomain(origin='*')
def predict():
	data = {"success": False}

	if flask.request.method == "GET":
		phr = flask.request.args['phrase']
		string = ""
		try:
			phil = requests.get(phr)
			phil.raise_for_status()
			p_elements = bs4.BeautifulSoup(phil.text,features="html5lib")
			print(1738)
			p_elements = p_elements.select('p')
			print(3)
			phr = p_elements
			for ele in p_elements:
				string += ele.getText()
			phr = string
		except Exception as exc:
			print("err with ele stuff p lol")
			pass

		phr = myNet.vecTor.transform([phr])
		prediction = ""
		with graph.as_default():
			prediction = myNet.nn.predict(phr)
		revMappings = {0:"worry",1:"neutral",2:"happiness",3:"sadness",4:"love",5:"surprise",6:"fun",7:"relief",8:"hate",9:"anger",10:"empty",11:"enthusiasm",12:"boredom"}
		prediction = prediction[0]
		maX = float('-inf')
		indeX = 0
		for index,pred in enumerate(prediction):
			if pred > maX:
				indeX = index
				maX = pred

		data["emotion"] = revMappings[indeX]
		data["superData"] = string
		data["success"] = True

	return flask.jsonify(data)


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
	print(("* Loading Keras model and Flask starting server..."
		"please wait until server has fully started"))
	load_model()
	app.run()
