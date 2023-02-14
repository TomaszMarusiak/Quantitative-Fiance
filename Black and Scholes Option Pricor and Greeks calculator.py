# Databricks notebook source
# MAGIC %md
# MAGIC Black and Scholes Option Pricor

# COMMAND ----------

# DBTITLE 1,Packages
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

k = 350
st = 360
r = 0.0329
t = 240/365
vol = 0.30

# COMMAND ----------

# DBTITLE 1,Black and Scholes Function create
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

# DBTITLE 1,Delta calculator
#create a function, type c=call, p=put
def delta(st,k,r,t,vol, type="C"):
  d1 = (np.log(st/k) + (r+(vol**2/2))*t)/(vol*np.sqrt(t))
  d2 = d1 - vol*np.sqrt(t)
#Calculate delta
  try:
    if type == "C":
      delta = norm.cdf(d1,0,1)
    elif type == "P":
      delta = -norm.cdf(-d1,0,1)
  except:
    print('Check the type')
    
  print('Delta: ',delta)

# COMMAND ----------

delta(600,599.4,0.0077,115/365,0.1697, type="C")

# COMMAND ----------

# DBTITLE 1,Gamma Calculator
def gamma(st,k,r,t,vol):
  d1 = (np.log(st/k) + (r+(vol**2/2))*t)/(vol*np.sqrt(t))
  d2 = d1 - vol*np.sqrt(t)
  try:
     gamma = norm.pdf(d1,0,1)/(np.sqrt(t)* vol* st)
  except:
    print('Check the type')
    
  print('gamma: ',gamma)

# COMMAND ----------

gamma(600,599.4,0.0077,115/365,0.1697)

# COMMAND ----------

# DBTITLE 1,Vega Calculator
def vega(st,k,r,t,vol):
  d1 = (np.log(st/k) + (r+(vol**2/2))*t)/(vol*np.sqrt(t))
  d2 = d1 - vol*np.sqrt(t)
  try:
    vega = st*norm.pdf(d1, 0, 1)*np.sqrt(t)
  except:
    print('Check the type')
    
  print('Vega: ',vega)

# COMMAND ----------

vega(600,599.4,0.0077,115/365,0.1697)

# COMMAND ----------

# DBTITLE 1,Theta Calculator
def theta(st,k,r,t,vol, type="C"):
  d1 = (np.log(st/k) + (r+(vol**2/2))*t)/(vol*np.sqrt(t))
  d2 = d1 - vol*np.sqrt(t)
  try:
    if type == "C":
      theta = -(st*norm.pdf(d1, 0, 1)*vol)/2*np.sqrt(t) - r*k*np.exp(-r*t)*norm.cdf(d2, 0 ,1)
    elif type == "P":
      theta = -(st*norm.pdf(d1, 0, 1)*vol)/2*np.sqrt(t) + r*k*np.exp(-r*t)*norm.cdf(-d2, 0 ,1)
  except:
    print('Check the type')
    
  print('Theta: ',theta)

# COMMAND ----------

theta(600,599.4,0.0077,115/365,0.1697)

# COMMAND ----------

# DBTITLE 1,Rho calculator
#create a function, type c=call, p=put
def rho(st,k,r,t,vol, type="C"):
  d1 = (np.log(st/k) + (r+(vol**2/2))*t)/(vol*np.sqrt(t))
  d2 = d1 - vol*np.sqrt(t)
  try:
    if type == "C":
      rho = k*np.t*np.exp(-r*t)*norm.pdf(d2, 0, 1)
    elif type == "P":
      rho = -k*np.t*np.exp(-r*t)*norm.pdf(-d2, 0, 1)
  except:
    print('Check the type')
    
  print('Rho: ',rho)

# COMMAND ----------

rho(600,599.4,0.0077,115/365,0.1697)
