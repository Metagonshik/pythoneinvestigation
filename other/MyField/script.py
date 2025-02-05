import json
import random
import string

def read_specification(spec_file):
    with open(spec_file, 'r') as file:
        spec_data = json.load(file)
    return spec_data

def generate_data(spec_data, output_file):
    with open(output_file, 'w') as file:
        for rule in spec_data['rules']:
            for _ in range(rule['count']):
                data = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(rule['length']))
                file.write(data + '\n')

if __name__ == '__main__':
    spec_file = '/home/rbatchaev/repo/pythonPlayground/other/MyField/specification.json'
    output_file = '/home/rbatchaev/repo/pythonPlayground/other/MyField/generated_data.txt'
    
    spec_data = read_specification(spec_file)
    generate_data(spec_data, output_file)
    
    print(f"Данные успешно сгенерированы и сохранены в файл '{output_file}'.")
