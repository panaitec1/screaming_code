import pandas as pd
import numpy as np

my_path = "E:\pythonwork\cognitive_ai\imports-85.data"
df = pd.read_csv(my_path, header = None)
#print(df)
#checking the top n rows of the dataframe
#showing the first 5 rows using dataframe.head() method

print("The first 5 rows of the dataframe are:")
print(df.head(5))

#checking the bottom n rows of the data frame using dataframe.tail() method
#print("The bottom 10 rows of the dataframe are:")
#print(df.tail(10))

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
#print("headers\n", headers)

#replacing automatically set headers with integers starting from 0
df.columns = headers
df.head(5)
df1 = df.replace("?", np.NaN)
df = df1.dropna(subset=["price"], axis = 0)
df.head(20)
print(df)

df.columns = headers
print(df.columns)

df.to_csv("E:/pythonwork/cognitive_ai/utomobile.csv", index = False)

#df = df.rename({"0":"symboling","1":"normalized-losses","2":"make","3":"fuel-type"}, axis = 1)
#print(df)


#We can drop missing values along the column "price" as follows:
#df = df1.dropna(subset=["price"],axis=0)
#df.head(20)

