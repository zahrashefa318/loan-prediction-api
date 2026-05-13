from model.model_loader import load_model
import numpy as np
def test_model_mathmatically():
    model=load_model()
    w=model["w"]
    b=model["b"]
    X_mean=model["X_mean"]
    x_std=model["X_std"]
    y_mean=model["Y_mean"]
    y_std=model["Y_std"]
    # let's create a sample input
    sample_input=[50000,10000,20000,4,5,30,1500,5000]
    normalized_input=(np.array(sample_input)-X_mean)/(x_std + 1e-8)
    predicted_normalized=np.dot(w,normalized_input)+b
    actual_prediction=predicted_normalized*y_std + y_mean
    actual_prediction=np.maximum(0,actual_prediction) # to avoid negative predictions.
    assert actual_prediction >= 0
    assert actual_prediction < 1000000
    assert isinstance(actual_prediction,np.float64)