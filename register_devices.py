"""
Set up all the desired objects in the FMC prior to adding the FTDs.
"""
from fmcapi import *
import logging

# ### Set these variables to match your environment. ### #
host = '192.168.11.2'
username = 'apiscript'
password = 'Admin123'
autodeploy = True

# ### Main Program ### #
with FMC(host=host, username=username, password=password, autodeploy=autodeploy) as fmc1:
    logging.info('# ### Register FTD(s) to the FMC ### #')

    # Register FTD to FMC
    device1 = Device(fmc=fmc1, name='daxmOffice', acp_name='Office', regKey='cisco123', hostName='192.168.11.3')
    device1.licensing(action='add', name='BASE')
    device1.licensing(action='add', name='THREAT')
    device1.licensing(action='add', name='VPN')
    device1.licensing(action='add', name='URLFilter')
    device1.licensing(action='add', name='MALWARE')
    device1.post()
