

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# data = {
#   "even": [2,4,6,8,10,12,14,16],
#   "odd": [1,3,5,7,11,13,17,19],
#   "no": [0,1,2,3,4,5,6,7]
# }

#load data into a DataFrame object:
# df = pd.DataFrame(data)
# x=df.drop('no',axis=1)
# y=df['no']
# print(x)
# print("----------------------")
# print(y)

# x_train, x_test, y_train, y_test = train_test_split(
#     x, y, test_size=0.2, random_state=42
# )
# print(x_train)
# print(x_test)
# print(y_train)
# print(y_test)

# print(df) 

data={
    
     "name":['nilam','shruti','snehal','saniya','shravni','ketan','tirth','shreyash','nikhil','tanmay'],
     "age":[51,55,57,58,62,63,65,67,68,70]
}
df = pd.DataFrame(data)
print(df)