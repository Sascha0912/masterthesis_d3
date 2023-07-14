import scipy.stats as stats
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import json
from sklearn.linear_model import LinearRegression


def ttest(data_group1, data_group2):
    return stats.ttest_ind(a=data_group1, b=data_group2, equal_var=True)


def mixedmodel(dataset):
    # data = sm.datasets.get_rdataset("dietox", "geepack").data
    # print(type(data))
    #print(str(dataset))
    dataset_string = json.dumps(dataset)
    # print(dataset_string)
    # print(type(dataset_string))

    df = pd.read_json(dataset_string, orient="records")
    # print(df)
    md = smf.mixedlm("value ~ id", df, groups=df["treatment"])
    mdf = md.fit()
    #print(mdf.summary())
    return mdf.summary()
    #return df


def linearregression(dataset):
    dataset_string = json.dumps(dataset)
    df = pd.read_json(dataset_string, orient="records")
    #print(df["id"].to_numpy())
    x = df["id"].to_numpy().reshape((-1, 1))
    y = df["value"].to_numpy()

    #print(x)
    #print(y)
    model = LinearRegression(fit_intercept=True).fit(x, y)
    #print(model)
    #print(model.score(x, y))
    #print(model.intercept_)
    #print(model.coef_)

    y_pred_1 = model.predict([[20]])
    y_pred_2 = model.predict([[21]])
    y_pred_3 = model.predict([[22]])

    #print(y_pred_1)
    #print(y_pred_2)

    return model.score(x, y), model.intercept_, model.coef_, y_pred_1, y_pred_2, y_pred_3
