from prophet import Prophet
import pickle as p

if __name__ == "__main__":
    modelname = 'PredictMidleMeasure.obj'

    with open(modelname, 'rb') as handle:
        unpickler = p.Unpickler(handle)
        m = unpickler.load()

    future = m.make_future_dataframe(periods=365)
    m.predict(future)






