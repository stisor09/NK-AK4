This is a bad collection of Python and Ansible scripts for setting up a small, (mostly) predetermined Cisco installation.

The things you should note to start off with is:

NK2-AK4-PySerial-Router 	#For the routers
NK2-AK4-PySerial-Layer3Switch	#For the Layer 3 Switch
NK2-AK4-PySerial-Layer2Switch	#For the Layer 2 Switches

These 3 scripts are used for configuring 2 routers, one Layer 3 Switch, and 2 Layer 2 Switches.
The way you use these requires a direct connection using an RS232-cable for console connection, where you will run the scripts to deploy configuration.
When you have deployed the configuration properly, you should have a functional internal network up and running, where you can SSH into each device.



At this point, you should look towards the Ansible part for automatic deeper configuration of these devices.
Inside the "Ansible" folder, you wil see several files. Keep all of them.
The only ones you need to worry about, are:

Site.yml
inventory.yml
"roles" and "groups" folder.
