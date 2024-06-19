import csv


def split_csv_by_date(input_file, date_column):
    data_by_date = {}
    headers = []
    infile = open(input_file, 'r')
    reader = csv.DictReader(infile, delimiter='|')
    headers = reader.fieldnames
    for row in reader:
        date = row[date_column]
        # Exclude the date column from the row data
        row_data = {key: value for key, value in row.items() if key != date_column}
        if date not in data_by_date:
            data_by_date[date] = []
        data_by_date[date].append(row_data)

    # Write separate files for each date
    for date, rows in data_by_date.items():
        output_file = f'{date}.csv'
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=[col for col in headers if col != date_column])
            writer.writeheader()
            writer.writerows(rows)
    print("Files have been created.")


split_csv_by_date('car_data.csv', 'Date')
