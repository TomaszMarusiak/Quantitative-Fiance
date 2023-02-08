
# COMMAND ----------

#import packages

import numpy as np
from scipy.stats import norm

# COMMAND ----------

#Variables

"""
k = strike price
st = spot price
r = risk free rate
t = maturity
vol = volitality
"""

#create a function, type c=call, p=put
def BSM(st,k,r,t,vol, type="C"):
  d1 = (np.log(st/k) + (r+(vol**2/2))*t)/(vol*np.sqrt(t))
  d2 = d1 - vol*np.sqrt(t)
  try:
    if type == "C":
      price = norm.cdf(d1,0,1)*st - norm.cdf(d2,0,1)*k*np.exp(-r*t)
    elif type == "P":
      price = -st*norm.cdf(-d1,0,1) + norm.cdf(-d2,0,1)*k*np.exp(-r*t)
  except:
    print('Check the type')
    
  print('Black and Scholes fair price is: ',price)

# COMMAND ----------

BSM(600,599.4,0.0077,115/365,0.1697, type="C")

# COMMAND ----------


