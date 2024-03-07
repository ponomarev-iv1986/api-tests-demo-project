import config
from helpers.load_certificate import load_cert
from helpers.load_json_body import load_body

uola_identification = {  # to be done
    'headers': {
        'RqUID': 'c7664d1d-4274-46af-a8a0-004eb113d72c',
        'SpName': 'dossbol-efs',
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': config.settings.PPRB_TOKEN,
    },
    'json': load_body('uola_identification.json'),
    'cert': (load_cert('rko-4g-tester.crt'), load_cert('rko-4g-tester.key')),
    # ('cert', 'key')
    'verify': load_cert('ca.pem'),  # 'to CA'
    'timeout': 480.0,
}

uola_generate_doc = {  # to be done
    'headers': {},
    'json': {},
    'cert': ('cert', 'key'),
    'verify': 'to CA',
    'timeout': 480.0,
}

uola_open_account = {  # to be done
    'headers': {},
    'json': {},
    'cert': ('cert', 'key'),
    'verify': 'to CA',
    'timeout': 480.0,
}
