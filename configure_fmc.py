"""
Set up all the desired objects in the FMC prior to adding the FTDs.
"""
from fmcapi import *
import logging

# ### Set these variables to match your environment. ### #
host = '192.168.11.2'
username = 'apiscript'
password = 'Admin123'
autodeploy = False

# ### Main Program ### #
with FMC(host=host, username=username, password=password, autodeploy=autodeploy) as fmc1:
    logging.info('# ### Configure Objects in FMC ### #')

    # Build Security Zones
    sz1 = SecurityZone(fmc=fmc1, name='IN', mode='ROUTED')
    sz1.post()
    sz2 = SecurityZone(fmc=fmc1, name='OUT', mode='ROUTED')
    sz2.post()

    # Build IP Objects
    ip1 = IPNetwork(fmc=fmc1, name='daxmNetworks', value='192.168.0.0/16')
    ip1.post()

    # Build Access Control Policies
    acp1 = AccessControlPolicy(fmc=fmc1, name='daxm corp')
    acp1.post()
    # Unfortunately we cannot nest ACPs yet via API.  That will have to be done manually.
    acp2 = AccessControlPolicy(fmc=fmc1, name='Office')
    acp2.post()
    # Currently we cannot create ACP parent/child relationships via API.  That needs to be done manually.

    # Build Access Control Policy Rules
    acprule1 = ACPRule(fmc=fmc1, name='INET Access', action='ALLOW', enabled=True)
    acprule1.acp(name=acp1.name)
    acprule1.source_zone(action='add', name=sz1.name)
    acprule1.destination_zone(action='add', name=sz2.name)
    acprule1.intrusion_policy(action='set', name='Security Over Connectivity')
    acprule1.source_network(action='add', name=ip1.name)
    acprule1.destination_network(action='add', name='any-ipv4')
    acprule1.logBegin = True
    acprule1.logEnd = True
    acprule1.post()

    # Build NAT Policy and Rules.
    # TBD