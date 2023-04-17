import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import  streamlit as st

st.set_page_config(
    page_title="Linear Regression Salary versus  ",
    page_icon="👋",
)

dataset = pd.read_csv("Salary_Data.csv")

dataset

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,:1].values

plt.plot(x, y, color = 'red')
plt.title("Salary vs Experience(Raw dataset)")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.show()


x_train,x_test, y_train,y_test = train_test_split(x, y, test_size = 1/4, random_state = 0 )

lin_regressor = LinearRegression()
lin_regressor.fit(x_train, y_train)

y_pred = lin_regressor.predict(x_test)

y_pred

plt.scatter(x_train, y_train, color = 'green')
plt.plot(x_train, lin_regressor.predict(x_train), color = 'red')
plt.title("Salary vs Experience(Train dataset)")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.show()

plt.scatter(x_test, y_test, color = 'green')
plt.plot(x_test, lin_regressor.predict(x_test), color = 'red')
plt.title("Salary vs Experience(Test dataset)")
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.show()











