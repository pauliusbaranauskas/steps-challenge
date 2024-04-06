# %%
import streamlit as st
import pandas as pd

from ipyvizzu import Chart, Data, Config, DisplayTarget
st.title('Steps by Paulius in 2024')

# %%
google_sheet_id = "1A2DKMRR6YMiDaDPutXJmykdhSnEpNBe6F6XJKUniqHw"
worksheet_name = "Steps_Challenge"

df = pd.read_csv(
    f"https://docs.google.com/spreadsheets/d/{google_sheet_id}/gviz/tq?tqx=out:csv&sheet={worksheet_name}"
)

df = df[~df["No. of steps"].isnull()]

df["Date"] = df["Date"].apply(pd.to_datetime)
df["No. of steps"] = df["No. of steps"].str.replace(",", "")
df["No. of steps"] = df["No. of steps"].apply(pd.to_numeric)
df["month"] = df["Date"].dt.month_name()
df["day of week"] = df["Date"].dt.day_name()
df["day of month"] = df["Date"].dt.day
df["week"] = df["Date"].dt.to_period("W")

df.head()

# %%

data = Data()
data.add_df(df, include_index="IndexColumnName")

chart = Chart(width="640px", height="360px", display=DisplayTarget.MANUAL)

chart.animate(data)

chart.animate(Config({"y": "No. of steps", "x":["month", "Date"], "geometry":"line"}))
chart.animate(Config({"geometry": "rectangle", "color": {"set":["month"]}}))

chart.animate(Config({"x": {"detach":["Date"]}}))


chart.animate(Config({"color":{"detach":"month"}, "x":{"detach":"month"}}))

# chart.animate(Config({}))

chart.animate(Config({"color":{"attach":"day of week"}}))

chart.animate(Config({"x":{"attach":["day of week"]}, "y":["mean(No. of steps)"]}))
chart.animate(Config({"geometry":"line", "color":{"detach":"day of week", "attach":"week"}, "y":["No. of steps"]}))


chart.feature("tooltip", True)
chart
# %%
