import pandas as pd

df = pd.DataFrame({
    'Date': ['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'],
    'Event': ['Music', 'Poetry', 'Theatre', 'Comedy'],
    'Cost': [10000, 5000, 15000, 2000]
})

# row_list = [[n, :] for n in range(df.shape[0])]
row_list = [df.iloc[n, :] for n in range(df.shape[0])]
print(row_list[:3])
