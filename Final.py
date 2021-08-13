import csv
import plotly.express as px
import pandas as pd

df = pd.read_csv("Data.csv")

mean = df.groupby(["studentid","level"], as_index = False)["attempt"].mean()

fig = px.scatter(mean, x = "studentid", y = "level", color = "attempt", size = "attempt")

fig.show()
