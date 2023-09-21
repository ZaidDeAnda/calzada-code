import pandas as pd

age_map = {
        "0_17" : "menor de 17",
        "18_65" : "adulto",
        "66MORE" : "mas de 66"
    }

column_map = {
    "SUBJECT" : "Edad",
    "LOCATION" : "País",
    "Value" : "Valor",
    "TIME" : "Año"
}

def read_poverty_df(path):
    df = pd.read_csv(path)
    df.drop("MEASURE", inplace=True, axis=1)
    df.drop("FREQUENCY", inplace=True, axis=1)
    df.drop("INDICATOR", inplace=True, axis=1)
    df.drop("Flag Codes", inplace=True, axis=1)

    df["SUBJECT"] = df["SUBJECT"].map(age_map)

    df = df.rename(columns=column_map)

    return df