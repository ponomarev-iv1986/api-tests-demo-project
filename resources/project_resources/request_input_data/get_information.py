import config
from helpers.load_certificate import load_cert
from helpers.load_json_body import load_body

get_information_completed = {
    'headers': {
        'uid': 'b2ccac1c-114f-4339-b393-3cdeb50aa7d4',
        'name': 'name',
        'Authorization': config.settings.TOKEN,
    },
    'json': load_body('user_body.json'),
    'cert': (load_cert('name.crt'), load_cert('name.key')),  # ('cert', 'key'),
    'verify': load_cert('ca.pem'),  # 'to CA'
    'timeout': 480.0,  # example
}

get_information_failed = {
    'headers': {},
    'json': {},
}  # to be done
