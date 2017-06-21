Steps:
    1. Boot up greenfield FMC.
    2. Enable 90 day licensing
    3. Create 'apiexplorer' and 'apiscript' Users.
    4. Run "configure_fmc.py"
    5. Run "register_devices.py"
    6. While waiting for devices to register build ACP hieracrchy, NAT Policy, NAT Rules.
    7. When registration(s) are complete associate devices to NAT Policy.
    8. Configure device's interfaces and routing.
    9. Save and Deploy.