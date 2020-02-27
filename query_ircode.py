import json
import os
"""
Dùng khi cập nhật smartir mới
"""
ROOT_DIR = './data'
path_smartir = os.path.join(ROOT_DIR, 'codes')
path_codes = os.path.join(ROOT_DIR, 'ircode.json')
folders = [f for f in os.listdir(path_smartir)]
ir_codes = {}
for files in folders:
    dem = 0
    # ir_codes[files] = {}

    path_files = os.path.join(path_smartir, files)
    if os.path.isfile(path_files) == False:
        file = [f for f in os.listdir(path_files)]
        # print(file)
        device = {}
        for fi in file:
            dem += 1
            try:
                with open(os.path.join(path_files, fi), 'r') as infile:
                    print(os.path.join(path_files, fi))
                    data = json.load(infile)
                    if data['supportedController'] == 'Broadlink':
                        if data['manufacturer'] not in device.keys():
                            device[data['manufacturer']] = {}
                            for i in data['supportedModels']:
                                device[data['manufacturer']][i] = fi.split('.')[
                                    0].strip()
                        else:
                            for i in data['supportedModels']:
                                device[data['manufacturer']][i] = fi.split('.')[
                                    0].strip()
            except Exception:
                print("Error file: ", os.path.join(path_files, fi))
                # print(len(device))
        ir_codes[files] = device
with open(path_codes, 'w') as outfiles:
    json.dump(ir_codes, outfiles)
