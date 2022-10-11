import json

import Settings
import Login
import EMailService

def exec(subject):
    conn = Login.login(subject)

    data = {
        "ymtys": "0", 
        "sfzx": "1",  
        "tw": "2",  
        "area": bytes(Settings.province, 'utf-8') + b'\x20' + bytes(Settings.city, 'utf-8') + b'\x20' + 
            bytes(Settings.area, 'utf-8'),
        "city": bytes(Settings.city, 'utf-8'),
        "province": bytes(Settings.province, 'utf-8'), 
        "address": bytes(Settings.address, 'utf-8'),  
        "sfcyglq": "0",  
        "sfyzz": "0",
        "qtqk": "",
        "askforleave": "0"
    }

    result = conn.post(
        url="https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/save",
        data=data
    )

    if result.status_code != 200:
        EMailService.send_email(subject + "Error!", "Please check information you have entered. Status code: " + result.status_code)
    else:
        try:
            result_json = json.loads(result.text)
            if result_json['e'] != 0:
                EMailService.send_email(subject + 'Error!', 'Error message: ' + str(result_json['e']) + '-' + result_json['m'])
                exit()
            else:
                EMailService.send_email(subject + "Finished!", "Wow! The " + subject + " have finished successfully!")
        except json.decoder.JSONDecodeError:
            exit()
