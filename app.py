import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import getdistance
import plotly.express as px

@st.cache
def fetch_and_clean_data(carpark,date_time):
# load model pickle to streamlit
    model = pickle.load(open('model2.pkl', 'rb'))
    prediction = model.predict([[carpark,date_time]])
    return prediction

@st.cache
def read_valuesfromCSV(allow_output_mutation=True):
    # load locaiton data csv
    df = pd.read_csv('/Users/rachpradhan/Downloads/Question 2 Submission/location_data.csv')
    return df
# input streamlit
locaitonDataFrame1 = read_valuesfromCSV()
locaitonDataFrame = locaitonDataFrame1
# st.write(locaitonDataFrame)
# convert items from locationDataFrame to list from Carpark_Number
carpark_list = locaitonDataFrame['Carpark_Number'].tolist()
# st.write("DB username:", st.secrets["URA_ACCEESTOKEN"])
st.title("Carpark Analysis Project")

st.subheader("Please enter the time and carpark you wish to find out information about")

p1, p2 = st.columns([1, 1])

# input streamlit
carpark_number = p1.selectbox("Carpark Number", carpark_list)
# find the row which has the carpark number
carpark_row = locaitonDataFrame.loc[locaitonDataFrame['Carpark_Number'] == carpark_number]
# st.write(carpark_row)
# get the carparkValue from that row
carparkValue = carpark_row['CarparkValue']

# st.write(carparkValue)
# input your date time 
# st.subheader("Please enter your date time")

# input streamlit
time = p2.time_input("Date Time")


# convert time to string in hours and minutes and seconds
# 
time = time.strftime("%H:%M:%S")
#remote the : from the time
time = time.replace(":","")
# remove any 0s in front of the time
time = time.lstrip("0")
# convert time to int
time = int(time)
# st.write(time) 

# Get your predicted value from the pickle

# Show your predicted value

predicted_value = fetch_and_clean_data(carparkValue,time)
# st.write(predicted_value)

# creatre a pyplot pie chart for 1-predicted_value and predicted_value
# # show the pie chart
# labels = ["You will find a carpark", "You will not find a carpark"]
# # create a pyplot bar chart for 1-predicted_value and predicted_value
# fig = plt.pie([predicted_value], colors=['green', 'red'])
# my_circle = plt.Circle((0,0), 0.7, color='white')
# fig = plt.gcf()
# fig.gca().add_artist(my_circle)
# my_circle = plt.Circle((0,0), 0.7, color='white')
# fig = plt.gcf()
# fig.gca().add_artist(my_circle)
#find the predicitons for the items in the following carpark values as well with the same time
# convert the carparkValue to a list
dataToLoad = locaitonDataFrame[locaitonDataFrame['dist']<4].sort_values(by='dist')[1:5]

dataLoadedList = dataToLoad['CarparkValue'].tolist()

# find the predictor for every item here
# st.write(dataLoadedList)
# st.write(time)
dataListTPredict = []
for items in dataLoadedList:
    print(items)
    predicted_value2 = fetch_and_clean_data(items,time)
    print(predicted_value2)
    dataListTPredict.append(predicted_value2)
dataToLoad['predicted_value'] = dataListTPredict

# for items in dataLoadedList:
#     st.write(items)
#     # predicted_value = fetch_and_clean_data(items,time)
#     # st.write(predicted_value)
#     dataToLoad['predicted_value'] = predicted_value
# st.write(dataToLoad)

# st.write(dataLoadedList)
with st.expander('View prediction results'):
    # st.write("The predicted value is", predicted_value[0])
    if(predicted_value>0.5):
        st.markdown(f"<h1><h3 style='text-align: center'>Carpark slots are available ✅</h3></h1>", unsafe_allow_html=True)
    else:     
        st.markdown(f"<h1><h3> Carpark slots are not availabke🛑 n</h3></h1>", unsafe_allow_html=True)
#give predicted value to 2dp 
with st.expander('View more details'):
    st.write( round(predicted_value[0],2),"% of the time you will find a carpark at this time")
    # s1, s2 = st.columns([1, 3])
    # s1.markdown(f"<h3 style='text-align: center; color: black;'>{predicted_value} (with {predicted_value} probability)</h1>", unsafe_allow_html=True)
    # s2.pyplot(fig)
with st.expander("The nearest and "):
    # st.write(dataToLoad)

#Apply distance function to dataframe
    # locaitonDataFrame['dist']=list(map(lambda k: getdistance.getDist(locaitonDataFrame.loc[k]['latitude'],locaitonDataFrame.loc[k]['longitude'],carpark_row['latitude'],carpark_row['longitude']), locaitonDataFrame.index))

    #This will give all locations within radius of 4 km arrange by distance
    # locaitonDataFrame[locaitonDataFrame['dist']<4].sort_values(by='dist')[0:5]
    # sort the data by predicted value
    # sort by predicted_value
    dataToLoad = dataToLoad.sort_values(by='predicted_value', ascending=False)
    # st.write(dataToLoad)

    fig = px.scatter_mapbox(locaitonDataFrame[locaitonDataFrame['dist']<4].sort_values(by='dist')[1:5], lat="latitude", lon="longitude", hover_name="Carpark_Number", hover_data=["Carpark_Number", "dist"],
                            color_discrete_sequence=["fuchsia"], zoom=10, height=500)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.map(dataToLoad)
    st.write(dataToLoad)



hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {
	
	visibility: hidden;
	
	}
footer:after {
	content:'Made with ❤️ by Team ';'; 
	visibility: visible;
	display: block;
	position: relative;
	#background-color: red;
	padding: 5px;
	top: 2px;
}
        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)