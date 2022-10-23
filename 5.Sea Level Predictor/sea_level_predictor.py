import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df = pd.read_csv("epa-sea-level.csv")
  y = df["CSIRO Adjusted Sea Level"]
  x = df["Year"]


    # Create scatter plot
  fig, ax = plt.subplots()
  plt.scatter(x,y)


    # Create first line of best fit
  res = linregress(x,y)
  print(res)
  x_pred = pd.Series([ i for i in range ( 1880 ,2050)])
  y_pred = res.slope * x_pred + res.intercept
  plt.plot(x_pred, y_pred, "r")


    # Create second line of best fit
  new_df = df.loc[ df['Year'] > 1999 ]
  new_y = new_df["CSIRO Adjusted Sea Level"]
  new_x = new_df["Year"]
  new_res = linregress(new_x,new_y)
  new_x_pred = pd.Series([ i for i in range ( 2000 ,2050)])
  new_y_pred = new_res.slope * new_x_pred + new_res.intercept
  plt.plot(new_x_pred, new_y_pred, "green")
  


    # Add labels and title
  ax.set_xlabel("Years")
  ax.set_ylabel("CSIRO Adjusted Sea Level")
  ax.set_title("Rise in Sea Level")


    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()