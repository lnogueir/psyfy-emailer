import csv
import os.path as path


def generate_csv(filename, data):
    print('GENERATING CSV: ', filename)
    open(filename, 'w').close()
    result_csv = open(filename, 'a')
    is_header = True
    for datapoint in data:
        if is_header:
            result_csv.write(','.join(list(datapoint.keys())))
            result_csv.write('\n')
            is_header = False
        result_csv.write(','.join(list(datapoint.values())))
        result_csv.write('\n')
    result_csv.close()
    print('CSV GENERATED: ', filename)


def get_list_from_csv(csv_doc):
    csv_headers = []
    result_data = []
    if path.exists(csv_doc):
        with open(csv_doc, encoding="ISO-8859-1") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for i, row in enumerate(csv_reader):
                if i == 0:
                    for j, col in enumerate(row):
                        if col.strip():
                            csv_headers.append(col.strip())
                else:
                    row_data = {}
                    for j, col in enumerate(row):
                        try:
                            if col.strip():
                                row_data[csv_headers[j]] = col.strip()
                        except:
                            break
                    if row_data not in result_data:
                        result_data.append(row_data)
    return result_data


def remove_duplicates_from_csv(filename):
    data = get_list_from_csv(filename)
    data_without_duplicates = []
    for datapoint in data:
        if datapoint not in data_without_duplicates:
            data_without_duplicates.append(datapoint)
    generate_csv(filename, data_without_duplicates)
