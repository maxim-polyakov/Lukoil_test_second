import pandas as pd

if __name__ == "__main__":
    df = pd.read_hdf('preloaded.hdf')
    df.to_csv('output.csv')