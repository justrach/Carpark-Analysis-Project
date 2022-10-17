# 1.1
Type of lots:
• C (for Cars)
• H (for Heavy Vehicles)
• Y (for Motorcycles)


# 1.2
```python
output_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ") #get the date time of the current time
data = req.get("https://api.data.gov.sg/v1/transport/carpark-availability?date_time=" + output_date ).json()

```

In order to get the DateTime of the entire object what we can do is basically utilise a list loop which would generate the dates from a given range, this can be done with the following code snippets

```python
date_list = pd.date_range(start="2022-08-01", end="2022-09-01", freq="H").strftime("%Y-%m-%dT%H:%M:%SZ").tolist()


```
And then to get the entire data list use this

```python
for i in date_list:
    output_date = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    data = req.get("https://api.data.gov.sg/v1/transport/carpark-availability?date_time=" + str(i) ).json()
    # print(data)
    #ignore if data[items] is empty
    #if data[items] is a key error, then it is empty
    

    try:
        if data['items'] == []:
            continue
        else:
            df = pd.DataFrame(data['items'][0])
            df.to_csv('data2.csv', mode='a', header=False, index=False)
    except KeyError:
        pass
```

# 1.3

# 1.4

