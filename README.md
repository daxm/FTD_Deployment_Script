# FTD_Deployment_Script
Use these scripts as a basis for a "Green Field" set up of an FMC and its FTD devices.

# Steps
 * Boot up greenfield FMC.
 * Enable 90 day licensing
 * Create 'apiexplorer' and 'apiscript' Users.
 * Run "configure_fmc.py"
 * Issue "configure manager add" command on FTD(s).
 * Run "register_devices.py"
 * While waiting for devices to register build ACP hieracrchy, NAT Policy, NAT Rules.
 * When registration(s) are complete associate devices to NAT Policy.
 * Configure device's interfaces and routing.  (I hope to automate this step soon!)
 * Save and Deploy.
 