import requests
from requests.packages import urllib3
import json

import Settings
import EMailService

urllib3.disable_warnings()

def login(subject):
    data = {
        "username": Settings.stu_id,
        "password": Settings.stu_passwd
    }

    try:
        conn = requests.Session()
        result_login = conn.post(
            url='https://xxcapp.xidian.edu.cn/uc/wap/login/check',
            data=data
        )
    except requests.exceptions.ConnectionError:
        EMailService.send_email(subject + "Login Error!", "Some connection errors occur, check your netword connection!")
        exit()

    if result_login.status_code != 200:
        EMailService.send_email(subject + ' Login Error!', 'Login error! Status code: ' + result_login.status_code)
        exit()
    else:
        try:
            login_json = json.loads(result_login.text)
            if login_json['e'] != 0:
                EMailService.send_email(subject + ' Login Error!', 'Login error! Error message: ' + str(login_json['e']) + '-' + login_json['m'])
                exit()
        except json.decoder.JSONDecodeError:
            exit()
    
    return conn