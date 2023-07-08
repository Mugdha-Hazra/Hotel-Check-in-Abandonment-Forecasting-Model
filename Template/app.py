from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# load the saved model
model = pickle.load(open("saved_model.pkl", "rb"))

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():
    # get the form data from the request
    country = request.form["country"]
    lead_time = int(request.form["lead_time"])
    previous_cancellations = int(request.form["previous_cancellations"])
    previous_bookings_not_canceled = int(request.form["previous_bookings_not_canceled"])
    booking_changes = int(request.form["booking_changes"])
    days_in_waiting_list = int(request.form["days_in_waiting_list"])
    try:
        adr = float(request.form["adr"])
    except ValueError:
        # Handle the exception appropriately (e.g., return an error message)
        return "Invalid input for adr parameter"
    required_car_parking_spaces = int(request.form["required_car_parking_spaces"])
    total_of_special_requests = int(request.form["total_of_special_requests"])
    total_customer = int(request.form["total_customer"])
    total_nights = int(request.form["total_nights"])
    try:
        deposit_given = float(request.form["deposit_given"])
    except ValueError:
        # Handle the exception appropriately (e.g., return an error message)
        return "Invalid input for adr parameter"
    # create a numpy array with the form data
    input_data = np.array(
        [
            [
                lead_time,
                previous_cancellations,
                previous_bookings_not_canceled,
                booking_changes,
                days_in_waiting_list,
                adr,
                required_car_parking_spaces,
                total_of_special_requests,
                total_customer,
                total_nights,
                deposit_given,
            ]
        ]
    )

    # make a prediction using the model
    prediction = model.predict(input_data)[0]
    prediction = request.json.get('prediction')
    
    if not isinstance(prediction, int):
        return jsonify({'error': 'Invalid input'}), 400
        
    # return the prediction as a JSON response
    response = {"prediction": prediction}
    return jsonify(response)


if __name__ == "__main__":
    app.run()

# from flask import Flask, request, jsonify, render_template
# import pickle
# import numpy as np
# import joblib

# # load the saved model
# # model = joblib.load('')
# model = pickle.load(open('saved_model.pkl', 'rb'))

# app = Flask(__name__)



# @app.route('/')
# def man():
#     return render_template('home.html')


# @app.route('/predict', methods=['GET','POST'])
# def home():
#     data1 = request.form['a']
#     data2 = request.form['b']
#     data3 = request.form['c']
#     data4 = request.form['d']
#     arr = np.array([[data1, data2, data3, data4]])
#     pred = model.predict(arr)
#     return render_template('after.html', data=pred)


# if __name__ == "__main__":
#     app.run(debug=True)

# # # create a Flask app
# # app = Flask(__name__)

# # # create an endpoint for receiving prediction requests
# # @app.route('/predict', methods=['POST'])
# # def predict():
# #     # get the input data from the request
# #     data = request.json

# #     # perform prediction on the input data using the loaded model
# #     prediction = model.predict(data)

# #     # return the prediction as a JSON response
# #     return jsonify(prediction.tolist())

# # # start the Flask app
# # if __name__ == '__main__':
# #     app.run(debug=True)
