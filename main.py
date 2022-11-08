import pandas
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')


data=pandas.read_csv('iphone_price.csv')
model=LinearRegression()
model.fit(data[['version']],data[['price']])

print('enter "0" to quit')

for i in range(100000):
    v=int(input('Enter verision: '))
    while v!=0:
        print('price: ',model.predict([[v]]))
        break
    if v==0:
        print('loop ended')
