import sys
import json

# JSON 데이터를 받아와서 계산 수행
def perform_calculation(json_data):
    print(json_data)
    data = json.loads(json_data)
    return json.dumps({'result': data})

# 명령줄 인수로 전달된 JSON 데이터 추출
json_data = sys.argv[1]
# 계산 수행 및 결과 출력
calculation_result = perform_calculation(json_data)
