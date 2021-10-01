import requests
import yaml
from pathlib import Path


class activateHelper:

    email = ''
    hostlink = "https://marketing.pt-ckit.com/api/get_activate.php"

    def __init__(self):
        self.email = self.getEmail()

    def getEmail(self):
        config = yaml.load(open(str(Path().absolute())+'/config/config.yaml', 'r'),
                           Loader=yaml.FullLoader)

        return config['email']

    def getName(self):
        config = yaml.load(open(str(Path().absolute())+'/config/config.yaml', 'r'),
                           Loader=yaml.FullLoader)

        return config['name']

    def getActivate(self):
        datas = {'email': self.email}
        dataret = {}
        try:
            resp = requests.post(self.hostlink, data=datas, timeout=None)

            retcode = resp.json()

            if(retcode['status'] == 'OK'):
                if retcode['subscribe'] == 'OK':
                    dataret = {
                        'active_text': "Anda berlangganan Aplikasi Ini mulai tanggal "+str(retcode['active_from'])+" hingga "+str(retcode['active_until'])+" (Sisa "+str(retcode['active_day'])+" Hari)"
                    }
                else:
                    dataret = {
                        'active_text': 'ERROR'
                    }
            else:
                dataret = {
                    'active_text': 'ERROR'
                }

        except requests.ConnectionError as error:
            print(error)
            dataret = {
                'active_text': 'ERROR'
            }

        return dataret
