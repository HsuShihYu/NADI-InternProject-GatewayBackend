import os
from configparser import ConfigParser



cfg = ConfigParser()

cfg.add_section('client config')
cfg.set('client config', "DA_INDEX",str(1))

with open('config.ini', 'w', encoding='utf-8') as file:
   cfg.write(file)
