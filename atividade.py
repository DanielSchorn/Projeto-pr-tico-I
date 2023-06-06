import csv

def load_data(file_name, separator):
    data = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file, delimiter=separator)
        for row in reader:
            data.append(row)
    return data

def save_data(file_name, data, separator):
    fieldnames = data[0].keys()
    with open(file_name, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=separator)
        writer.writeheader()
        writer.writerows(data)

def convert_value(value, data_type):
    try:
        if data_type == 'str':
            return str(value)
        elif data_type == 'int':
            return int(value)
        elif data_type == 'float':
            return float(value)
        else:
            return value
    except ValueError:
        return value

def convert_data_types(data, column_types):
    converted_data = []
    for row in data:
        converted_row = {}
        for key, value in row.items():
            data_type = column_types.get(key, 'str')
            converted_row[key] = convert_value(value, data_type)
        converted_data.append(converted_row)
    return converted_data

def access_data_by_index(data, indices):
    return [data[index] for index in indices]

def filter_data(data, condition):
    return [row for row in data if condition(row)]

def project_data(data, columns):
    return [{column: row[column] for column in columns} for row in data]

def update_data(data, condition, updates):
    for row in data:
        if condition(row):
            for key, value in updates.items():
                row[key] = value

def group_data(data, key):
    grouped_data = {}
    for row in data:
        group_value = row.get(key)
        if group_value not in grouped_data:
            grouped_data[group_value] = []
        grouped_data[group_value].append(row)
    return grouped_data