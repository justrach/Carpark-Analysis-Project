import requests as req
import datetime
import pandas as pd

import streamlit as st

st.title("Test Data")
#Get the current date time
output_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
val = "YYYY-MM-DD[T]HH:mm:ss"
val = "2022-10-06T10:51:34.765Z"
print(str(output_date))
# Get the data from the API
data = req.get("https://api.data.gov.sg/v1/transport/carpark-availability?date_time=" + val ).json()

# st.write(data)



# To convert data to a dataframe
df = pd.DataFrame(data['items'][0]['carpark_data'])
# To read items inside carpark_info dataframe
print(df)

st.write(df)


