# Tutorial https://realpython.com/python-dash/#how-to-build-a-dash-application

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Descargar https://lmorillas.github.io/dwes/docs/dash/aguacates/avocado.csv
# DataFrame
data = pd.read_csv("datos/avocado.csv")
data = data.query("type == 'conventional' and region == 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

app = Dash(__name__)

if __name__ == '__main__':
    app.run_server(debug=True)