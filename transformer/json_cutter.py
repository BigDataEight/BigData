import json

def slice_json_file(json_filepath, start_row, end_row, output_filepath):
    with open(json_filepath, 'r') as json_file, open(output_filepath, 'w') as output_file:
        for i, line in enumerate(json_file):
            if i >= start_row and i < end_row:
                output_file.write(line)
            elif i >= end_row:
                break
            
json_filepath = 'python_bigdata\\BigData\\imu.json'

output_filepath = 'python_bigdata\\BigData\\imu_temp.json'

slice_json_file(json_filepath, 0, 100, output_filepath)