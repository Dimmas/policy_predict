import pandas as pd
import dill as pickle
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/predict', methods = ['POST'])
def api_call():
    try:
        req_json = request.get_json()
        input_data = pd.read_json(req_json, orient='records')
    except Exception as e:
        raise e

    clf = 'policy_knn.pk'

    if input_data.empty:
        return 'zero json'
    else:
        loaded_model = None
        with open('./models/'+clf, 'rb') as f:
            loaded_model = pickle.load(f)
        policy_pred = loaded_model.predict(input_data)
        responses = jsonify(predictions=policy_pred.to_json(orient="records"))
        responses.status_code = 200

        return responses
