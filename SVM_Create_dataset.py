import pandas as pd

file1 = "input_Dataset.CSV"

xl1 = pd.read_csv(file1)

Change,Index_Momentum,Index_Volatility,Sector_Momentum,Stock_Momentum,Stock_Price_Volatility,Stock_Sales_Close

date_1 = xl1['Date']
Close_1 = xl1['Close']
Change_1 = xl1['Change']
Momentum_1 = xl1['Momentum']