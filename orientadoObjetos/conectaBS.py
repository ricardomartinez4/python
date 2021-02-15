# -*- coding: utf-8 -*-
'''
https://pypi.org/project/keyring/

Dónde se localiza el fichero:
    python -c "import keyring.util.platform_; print(keyring.util.platform_.config_root())"
    python -c "import keyring.util.platform_; print(keyring.util.platform_.data_root())"
'''
import keyring

try: 
    keyring.get_keyring()
    keyring.set_password("mysql", "ricardomartinez4", "1234")
    print(keyring.get_password("mysql", "ricardomartinez4"))
except Exception as e:
    print('Error: {}'.format(e))
    