import requests


def verify(phone, code):
    url = "http://notify.eskiz.uz/api/message/sms/send"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDQ4MDk0ODAsImlhdCI6MTcwMjIxNzQ4MCwicm9sZSI6InVzZXIiLCJzdWIiOiIxMDUzIn0.68hdV55gTrUTvnV4VoUTIhzUxWuHIejPOvefUW7abzU"}
    data = {
        'mobile_phone': phone,
        'message': code,
        'from': "4546",
        'callback_url': 'http://0.0.0.0.uz/test.php'
    }

    response = requests.post(url=url, data=data, headers=headers)
    return response
