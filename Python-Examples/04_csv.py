import csv
from datetime import datetime

csv_path = "/Users/sfm/Documents/Python-Lessons/Python-Examples/google_stock_data.csv"
csv_file = open(csv_path, newline='')
csv_reader = csv.reader(csv_file)
csv_file_header = next(csv_reader)
# csv_file_data = [row for row in csv_reader]

csv_data = []
for row in csv_reader:
    trade_date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high_price = float(row[2])
    low_price = float(row[3])
    close_price = float(row[4])
    volume_trd = float(row[5])
    adj_close = float(row[6])

    csv_data.append([trade_date, open_price, high_price,
                     low_price, close_price, volume_trd, adj_close])

# print(csv_data[0])

returns_path = "./returns.csv"
returns_file = open(returns_path, 'w')
csv_writer = csv.writer(returns_file)

csv_writer.writerow(["Date", "Return"])

for i in range(len(csv_data) - 1):
    todays_row = csv_data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[6]

    yesterdays_row = csv_data[i + 1]
    yesterdays_price = yesterdays_row[6]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    formatted_date = todays_date.strftime('%m/%d/%Y')

    csv_writer.writerow([formatted_date, daily_return])

# print(csv_file_header)
# print(csv_file_data[0])

# lines = [line.strip().split(',') for line in csv_file]

# print(lines[1])
# for line in csv_file:
# print(line)
