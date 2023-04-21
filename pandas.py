import pandas as pd

#create init dataframe df1 and df2
#create a view df2 from df1
df1 = pd.DataFrame({"c1":[1,2], "c2":[3,4]})
df2 = df1["c1"] 

#change the value of df2 using iloc
df2.iloc[0] = 7

#check final value from df1
df1 


#pandas 2.0
pandas.option.mode.copy_on_write = True
