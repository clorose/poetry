# 예시: test.py 파일에 requests 라이브러리 사용하기

import requests

response = requests.get('https://www.example.com')
print(response.status_code)
