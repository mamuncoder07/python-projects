import json

if __name__ == '__main__':
    try:
        with open('Subject.json', 'r') as f:
            data = json.loads(f.read())

        # Header create karega automatically
        output = ','.join([*data[0]])

        # Data rows add karega
        for obj in data:
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'

        # CSV file write karega
        with open('output.csv', 'w') as f:
            f.write(output)

        print("CSV file successfully created ✅")

    except Exception as ex:
        print(f'Error: {str(ex)}')
