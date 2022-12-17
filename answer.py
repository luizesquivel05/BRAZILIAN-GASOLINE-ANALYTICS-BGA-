import pandas as pd

# PRE QUESTIONS:
def centralData():
    anos2000 = pd.read_csv("Data/gasolina_2000+.csv", index_col=0)
    anos2010 = pd.read_csv("Data/gasolina_2010+.csv", index_col=0)
    gasolinaData = pd.concat([anos2000, anos2010])
    gasolinaData["DATA INICIAL"] = pd.to_datetime(gasolinaData["DATA INICIAL"])
    gasolinaData["DATA FINAL"] = pd.to_datetime(gasolinaData["DATA FINAL"])
    gasolinaData.fillna(0, inplace=True)
    gasolinaData["ANO-MES"] = gasolinaData["DATA FINAL"].apply(lambda x: "{}".format(x.year)) + gasolinaData["DATA FINAL"].apply(lambda x: "-{:02d}".format(x.month))
    
    return gasolinaData

# FIRST QUESTION:
def frequency():
    data = centralData()
    return data["PRODUTO"].value_counts()
    
# SECOND QUESTION:
def commom():
    data = centralData()
    return data[data["PRODUTO"] == 'GASOLINA COMUM']

# THIRD QUESTION:
def auguste2008():
    data = centralData()
    return data[data["ANO-MES"] == '2008-08']["PREÇO MÉDIO REVENDA"].mean()

# FOURTH QUESTION:
def may2014SP():
    data = centralData()
    return data[(data["ANO-MES"] == '2008-08') & (data["ESTADO"] == 'SAO PAULO')]["PREÇO MÉDIO REVENDA"].mean()

# FIFTH QUESTION:
def flagExceeded():
    data = centralData()
    return data[data["PREÇO MÉDIO REVENDA"] > 5][["ESTADO", "ANO-MES", "PREÇO MÉDIO REVENDA"]].head(5)

# SIXTH QUESTION:
def meanpriceofSOUTH():
    data = centralData()
    aux = data[(data["DATA FINAL"].apply(lambda x: x.year) == 2012)]
    return aux[aux["REGIÃO"] == "SUL"]["PREÇO MÉDIO REVENDA"].mean()

# SEVENTH QUESTION:
def yeartoyearRJ():
    data = centralData()
    data["MES"] = data["DATA FINAL"].apply(lambda x: x.month)
    rio = data[data["ESTADO"] == "RIO DE JANEIRO"]
    month_rio = rio.groupby("ANO-MES")[["PREÇO MÉDIO REVENDA", "MES"]].last()
    return (month_rio[month_rio["MES"] == 12] / month_rio[month_rio["MES"] == 12].shift(1) - 1) * 100

# EIGHTH QUESTION: 
def diferencePrices():
    data = centralData()
    maxI = data.groupby('ANO-MES')["PREÇO MÉDIO REVENDA"].idxmin()
    return data.loc[maxI, :][["ESTADO", "PREÇO MÉDIO REVENDA", "ANO-MES"]]