import csv
import datetime

with open('sample.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    data = [(int(col1), int(col4), col5.split('/')[4], datetime.datetime.strptime(col6, "%Y-%m-%d").date()) for col1, col2, col3, col4, col5, col6, col7 in reader]
    print(data)
    import pdb; pdb.set_trace()
