import requests
import yaml
from pathlib import Path


class activateHelper:

    email = ''
    hostlink = "https://marketing.pt-ckit.com/api/get_activate.php"
    # hostlink = "http://localhost/marketplace/api/get_activate.php"

    def __init__(self):
        self.email = self.openconfig("email")

    def openconfig(self, val):
        config = yaml.load(open(str(Path().absolute())+'/config/config.yaml', 'r'),
                           Loader=yaml.FullLoader)

        return config[val]

    def getActivate(self):
        datas = {'email': self.email}
        dataret = {}
        try:
            resp = requests.post(self.hostlink, data=datas, timeout=None)

            retcode = resp.json()

            if(retcode['status'] == 'OK'):
                if retcode['subscribe'] == 'OK':
                    dataret = {
                        'active_status': 'OK',
                        'active_text': "Anda berlangganan Aplikasi Ini mulai tanggal "+str(retcode['active_from'])+" hingga "+str(retcode['active_until'])+" (Sisa "+str(retcode['active_day'])+" Hari)"
                    }
                else:
                    dataret = {
                        'active_status': 'ERROR',
                        'active_text': 'YOUR SUBSCRIPTION HAS ENDED'
                    }
            else:
                dataret = {
                    'active_status': 'ERROR',
                    'active_text': 'USER NOT FOUND CHECK YOUR EMAIL'
                }

        except requests.ConnectionError as error:
            dataret = {
                'active_status': 'ERROR',
                'active_text': error
            }

        return dataret
