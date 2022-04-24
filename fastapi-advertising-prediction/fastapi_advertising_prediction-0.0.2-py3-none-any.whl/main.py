from fastapi import FastAPI, Request
from fastapi_advertising_prediction.schemas import Advertising
import joblib
import uvicorn

# Read models saved during train phase
estimator_advertising_loaded = joblib.load(
    "fastapi_advertising_prediction/saved_models/03.randomforest_with_advertising.pkl")

app = FastAPI()


def make_advertising_prediction(model, request):
    # parse input from request
    TV = request["TV"]
    Radio = request['Radio']
    Newspaper = request['Newspaper']

    # Make an input vector
    advertising = [[TV, Radio, Newspaper]]

    # Predict
    prediction = model.predict(advertising)

    return prediction[0]


# Advertising prediction endpoint
@app.post("/prediction/advertising")
def predict_iris(request: Advertising):
    prediction = make_advertising_prediction(estimator_advertising_loaded, request.dict())
    return prediction


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True,
                log_level="debug", debug=True,
                workers=1, limit_concurrency=1, limit_max_requests=1)
