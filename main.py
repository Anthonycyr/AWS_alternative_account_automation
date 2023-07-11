import boto3
import pandas as pd

#Mettre le bon nom du fichier
dataframe = pd.read_csv('./fakedata.csv')

dataframe = dataframe.melt(id_vars='AccountId', var_name='Type', value_name='Email')
sorted_dataframe = dataframe.sort_values(by='AccountId')
sorted_dataframe['AccountId'] = sorted_dataframe['AccountId'].astype(str)
sorted_dataframe.to_csv('./melted_data.csv', index=False)
print(dataframe)

for index, row in sorted_dataframe.iterrows():
    accountId= row['AccountId']
    alternateContactType = row['Type']
    email=  row['Email']
    print(accountId)

    client = boto3.client('account')

    response = client.put_alternate_contact(
        AccountId=accountId,
        AlternateContactType= alternateContactType,
        EmailAddress= email,
        Name= alternateContactType,
        PhoneNumber='514-499-5053',
        Title=alternateContactType
    )
    print(response)



