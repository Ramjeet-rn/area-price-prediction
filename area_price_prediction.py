import pandas as pd
from sklearn.linear_model import LinearRegression

data=pd.read_csv('area_prices.csv')
X=data[['Area']]
y=data['Price']
model=LinearRegression()
model.fit(X,y)
area=float(input('Enter Area (sq ft): '))
price=model.predict([[area]])
print(f'Predicted Price: ₹{price[0]:,.2f}')
