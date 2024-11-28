import pandas as pd
from prophet import Prophet
import pickle as p

if __name__ == "__main__":
    df = pd.read_csv('output.csv')
    d = {'ds': df['TimeStamp'], 'y': df['target']}
    rdf = pd.DataFrame(data=d)
    m = Prophet()
    m.fit(rdf)
    future = m.make_future_dataframe(periods=365)
    m.predict(future)

    modelname = 'PredictMidleMeasure.obj'
    with open(modelname, 'wb') as handle:
        p.dump(m, handle, protocol=p.HIGHEST_PROTOCOL)






