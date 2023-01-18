import os
import json
from alive_progress import alive_bar

SUB_FOLDER = 'react'

PATH = 'analyzed_files/' + SUB_FOLDER

# "LAYER" | "LENGTH" | "TEST"
CHOICE = "LENGTH"

print(f'doing {CHOICE} at {PATH}')

try:
    os.makedirs(f'processed_data/{SUB_FOLDER}/{CHOICE}')
except FileExistsError:
    pass

DATA_COMP = {
    'A1': 1,
    'A2': 2,
    'B1': 3,
    'B2': 4,
    'C1': 5,
    'C2': 6,
}

list_dir = os.listdir(PATH)

dim_y = []
dim_x = []

if CHOICE == 'LAYER' or CHOICE == 'LENGTH':
    with alive_bar(len(list_dir)) as bar:
        for file_dir in list_dir:
            with open(f'{PATH}/{file_dir}', 'r') as file:
                json_data = json.load(file)
                for file_name, file_data in json_data.items():
                    for construct in file_data:
                        mock = 'test/react/fixtures/art/VectorWidget.js'
                        if construct['Level'] == 'A1' or construct['Level'] == 'A2':
                            pass
                        else:
                            if CHOICE == 'LAYER':
                                file_name = file_name.replace('//', '')
                                dim_x_data = file_name.count('/') - 1
                                dim_y.append(DATA_COMP[construct['Level']])
                                dim_x.append(dim_x_data)
                            elif CHOICE == 'LENGTH':
                                dim_x_data = len(file_name)
                                dim_y.append(DATA_COMP[construct['Level']])
                                dim_x.append(dim_x_data)
            bar()

    with open(f'processed_data/{SUB_FOLDER}/{CHOICE}/dim_x.json', 'w') as file:
        file.write(json.dumps((dim_x), indent=4))

    with open(f'processed_data/{SUB_FOLDER}/{CHOICE}/dim_y.json', 'w') as file:
        file.write(json.dumps((dim_y), indent=4))

elif CHOICE == 'TEST':
    with alive_bar(len(list_dir)) as bar:
        for file_dir in list_dir:
            with open(f'{PATH}/{file_dir}', 'r') as file:
                json_data = json.load(file)
                for file_name, file_data in json_data.items():
                        for construct in file_data:
                            if construct['Level'] == 'A1' or construct['Level'] == 'A2':
                                pass
                            else:
                                if 'test' in file_name[4:]:
                                    dim_x.append(DATA_COMP[construct['Level']])
                                else:
                                    dim_y.append(DATA_COMP[construct['Level']])
            bar()

    with open(f'processed_data/{SUB_FOLDER}/{CHOICE}/test.json', 'w') as file:
        file.write(json.dumps((dim_x), indent=4))

    with open(f'processed_data/{SUB_FOLDER}/{CHOICE}/non_test.json', 'w') as file:
        file.write(json.dumps((dim_y), indent=4))
