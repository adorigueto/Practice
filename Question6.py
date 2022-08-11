import numpy as np
from sklearn import linear_model

def desired_marketing_expenditure(marketing_expenditure, units_sold, desired_units_sold):
    """
    :param marketing_expenditure: (list) A list of integers with the expenditure for each previous campaign.
    :param units_sold: (list) A list of integers with the number of units sold for each previous campaign.
    :param desired_units_sold: (integer) Target number of units to sell in the new campaign.
    :returns: (float) Required amount of money to be invested.
    """
    reg = linear_model.LinearRegression()
    exp = np.array(marketing_expenditure).reshape(-1,1)
    uni = np.array(units_sold).reshape(-1,1)
    reg.fit(uni, exp)
    des_mkt_exp = reg.predict(np.array([desired_units_sold]).reshape(-1,1))[0,0].round(-2)
    des_mkt_exp.astype(float)
    print(type(des_mkt_exp))
    return des_mkt_exp

#For example, with the parameters below, the function should return 250000.0
print(desired_marketing_expenditure(
    [300000, 200000, 400000, 300000, 100000],
    [60000, 50000, 90000, 80000, 30000],
    60000))

reg = linear_model.LinearRegression()
exp = np.array([300000, 200000, 400000, 300000, 100000]).reshape(-1, 1)
uni = np.array([60000, 50000, 90000, 80000, 30000]).reshape(-1, 1)
reg.fit(uni, exp)
reg.score(uni, exp)
reg.predict(uni)
reg.predict(np.array([60000]).reshape(-1,1)).astype(int)
