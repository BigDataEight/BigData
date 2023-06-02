import csv
import json
from datetime import datetime

def convert_csv_to_json(csv_filepath, json_filepath, chunk_size=10000):
    now = 10000
    with open(csv_filepath, 'r') as csv_file, open(json_filepath, 'w') as json_file:
        csv_reader = csv.DictReader(csv_file)
        json_data = []
        row_count = 0
        
        for row in csv_reader:

            # 데이터가 너무커서 10초단위로 저장합니다.
            check = row['시간']
            check = check[-1:]
            check = int(check)
            if check != 0 :
                continue

            # 센서명 분석하기 쉽게 변경
            name = row['센서명']
            name = name[-8:]
            row['name'] = name
            del row['센서명']

            # 시간 Date 자료형으로 저장
            date_str = row['시간']
            date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            row['date'] = {"$date": date_obj.isoformat()}
            del row['시간']

            # 특정 필드의 자료형을 double로 변환
            row['위도'] = float(row['위도'])  
            row['경도'] = float(row['경도'])  
            row['가속도엑스축'] = float(row['가속도엑스축'])  
            row['가속도와이축'] = float(row['가속도와이축'])  
            row['가속도제트축'] = float(row['가속도제트축'])  
            row['자이로엑스축'] = float(row['자이로엑스축'])  
            row['자이로와이축'] = float(row['자이로와이축'])  
            row['자이로제트축'] = float(row['자이로제트축'])  
            row['마그네틱엑스축'] = float(row['마그네틱엑스축'])  
            row['마그네틱와이축'] = float(row['마그네틱와이축'])  
            row['마그네틱제트축'] = float(row['마그네틱제트축'])  

            # 위도와 경도를 location 필드로 embedded 타입으로저장
            location = {
                "latitude": row['위도'],
                "longitude": row['경도'],
                "geohash": row['지오해시']
            }
            row['location'] = location
            del row['위도']
            del row['경도']
            del row['지오해시']

            # 가속도엑스축, 가속도와이축, 가속도제트축를 acceleration 필드로 묶기
            acceleration = {
                "x": row['가속도엑스축'],
                "y": row['가속도와이축'],
                "z": row['가속도제트축']
            }
            row['acceleration'] = acceleration
            del row['가속도엑스축']
            del row['가속도와이축']
            del row['가속도제트축']

            # 자이로엑스축, 자이로와이축, 자이로제트축를 gyro 필드로 묶기
            gyro = {
                "x": row['자이로엑스축'],
                "y": row['자이로와이축'],
                "z": row['자이로제트축']
            }
            row['gyro'] = gyro
            del row['자이로엑스축']
            del row['자이로와이축']
            del row['자이로제트축']

            # 마그네틱엑스축, 마그네틱와이축, 마그네틱제트축를 magnetic 필드로 묶기
            magnetic = {
                "x": row['마그네틱엑스축'],
                "y": row['마그네틱와이축'],
                "z": row['마그네틱제트축']
            }
            row['magnetic'] = magnetic
            del row['마그네틱엑스축']
            del row['마그네틱와이축']
            del row['마그네틱제트축']

            json_data.append(row)
            row_count += 1

            # 시, 군구, 동 address 필드로 묶기

            address = {
                "city": row['시'],
                "gungu": row['군구'],
                "dong": row['동']
            }
            row['address'] = address
            del row['시']
            del row['군구']
            del row['동']

            # 일정한 개수만큼 데이터를 모았을 때 JSON 파일로 저장
            if row_count % chunk_size == 0:
                json.dump(json_data, json_file)
                json_file.write('\n')
                json_data = []
                print(now)
                now += 10000
                break;
        
        
        # 마지막에 남은 데이터를 JSON 파일로 저장
        json.dump(json_data, json_file)
        json_file.write('\n')

# CSV 파일 경로
csv_filepath = 'python_bigdata\\BigData\\imu.csv'

# JSON 파일 경로
json_filepath = 'python_bigdata\\BigData\\imu6.json'

# CSV 파일을 JSON으로 변환
convert_csv_to_json(csv_filepath, json_filepath)