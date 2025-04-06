This is a bad collection of Python and Ansible scripts for setting up a small, (mostly) predetermined Cisco installation.

The things you should note to start off with is:

NK2-AK4-PySerial-Router 	#For the routers
NK2-AK4-PySerial-Layer3Switch	#For the Layer 3 Switch
NK2-AK4-PySerial-Layer2Switch	#For the Layer 2 Switches

These 3 scripts are used for configuring 2 routers, one Layer 3 Switch, and 2 Layer 2 Switches.
The way you use these requires a direct connection using an RS232-cable for the console, where you will run the scripts to deploy configuration.

NOTE!!!
When creating your "hostname" for your devices when running the Python scripts make sure to do the following:

Router 1 is named "Router1"
Router 2 is named  "Router2"

Layer 3 switch is named "Layer3Switch"

Your first layer 2 switch is named "Layer2Switch1"
Your second layer 2 switch is named "Layer2Switch2"

This is necessary for the Ansible script to work properly on certain configurations. If you want to use other hostnames, you must alter the .yml scripts as needed.
The same applies for SSH login information. Keep it 'cisco' on username and password. If you want to use other login data, you must alter the .yml scripts as needed.
NOTE!!

When you have deployed the configuration properly, you should have a functional internal network up and running, where you can SSH into each device.

At this point, you should look towards the Ansible part for automatic deeper configuration of these devices.

Inside the "Ansible" folder, you wil see several files. Keep all of them.

The only ones you need to worry about, are:

Site.yml
inventory.yml
"roles" and "groups" folder.

The "site.yml" file is the one you should run using the ansible-playbook command.

It contains directories to other .yml files to run that configures your network devices. These directories are inside the "roles" folder.

The "inventory.yml" file contains the hosts, the network devices that Ansible will interact with. It includes their hostname, IP addressing, and SSH login information.

The "roles" folder splits up for routers and switches, and each have their own configuration.

The contents of the .yml files can be altered, but keep in mind:

	lines:
	 - These are the same as inputting commands in a CLI directly on the device.

	parents: This is the same as specifying WHERE you input commands. Look at hsrp.yml or dhcp.yml for examples.

	when: A variable choice of "When something happens, do the following". Look at port_config.yml for an example.

Expanding or adding new .yml scripts is as simple as copying existing code used elsewhere, and altering the values to fit your needs.



The "groups" folder is pretty much obsolete since the "inventory.yml" file contains what is necessary.
