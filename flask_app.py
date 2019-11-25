# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
# import pickle
from sklearn.externals import joblib
import pandas as pd
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Load the model
# model = pickle.load(open('model.pkl','rb'))
model = joblib.load(open('/home/samuelnatami/mysite/model.pkl','rb'))

@app.route('/api',methods=['POST'])
@cross_origin()
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)


    # Make prediction using model loaded from disk as per the data.
    # prediction = model.predict(data[['duration_in_month','credit_amount','unemployed','installment_as_income_perc','present_res_since','age','credits_this_bank','people_under_maintenance','foreign_worker_yes']])

    # print(data.values())

    prediction = model.predict([list(data.values())])
    # Take the first value of prediction
    output = prediction[0]

    return jsonify({"result": str(output)})

# if __name__ == '__main__':
#     try:
        # app.run(port=5000, debug=True)
#     except:
#         print("Server is exited unexpectedly. Please contact server admin.")


# if __name__ == '__main__':
#     app.debug = True
#     app.run()