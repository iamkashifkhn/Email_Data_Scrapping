import pandas as pd
import email


df = pd.read_csv('emails.csv')
df = df.head(1000)
df.shape

# message = df.loc[0]['message']
# e = email.message_from_string(message)
# # print(e)
# print(e.items())

def get_field(field, messages):
    coloumn = []
    for message in messages:
        e= email.message_from_string(message)
        coloumn.append(e.get(field))
    return coloumn

def get_body(messages):
    coloumn = []
    for message in messages:
        e= email.message_from_string(message)
        coloumn.append(e.get_payload())
    return coloumn


df['Date'] = get_field("Date", df['message'])
df['From'] = get_field("From", df['message'])
df['To'] = get_field("To", df['message'])
df['Subject'] = get_field("Subject", df['message'])
df['Body'] = get_body(df['message'])
# print(df.head(3))
# del df['Unnamed']
# del df['Unnamed: 0']
del df['message']
del df['file']
pd.DataFrame(df).to_csv('Output2.csv')
myOutput = pd.read_csv('Output2.csv', index_col=False)
print(myOutput)

