# AWS_alternative_account_automation

Automation to put alternative account information using python sdk boto3.

Takes a spread sheet as .csv files and makes a request to push information into the management account.

## prerequiste
- a .csv file with this structure: AccountId,Security,Operations,Billing (fakedata.csv for an example)
- enough permission to make this change into every account found in the sread sheet