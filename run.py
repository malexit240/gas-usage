import json as js
from datetime import datetime


def round(value):
    return "%.2f" % value

with open('data.json','rt') as file:
    data = js.loads(file.read())

    gas = data['gas1'] - data['gas2']
    
    date1 = datetime.strptime(data['date1'],'%d/%m/%y %H:%M:%S')
    date2 = datetime.strptime(data['date2'],'%d/%m/%y %H:%M:%S')

    ellapsed_time = (date1 - date2).total_seconds() / 60 / 60

    price = 9.7

    gas_usage_per_hour = gas/ellapsed_time
    
    print(f'Ellapsed time: {round(ellapsed_time)} hours')
    print(f'Used gas: {round(gas_usage_per_hour)} m3')
    print(f'Potential pay for month:{round(gas_usage_per_hour * 24 * 31 * price)} UAH')