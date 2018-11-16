from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np

def forecast(input, steps):
    model = ARIMA(input, order=(4,1,0))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast(steps)
    return output[0]
