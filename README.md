Policy Conversion from Palo Alto to Fortigate
When converting the policy from Palo Alto, we need to consider a few things:

Type → This is not present in Fortigate.
Subnets added individually in a policy on Palo Alto cannot be added directly to Fortigate. All subnets must be considered as Addresses and Address Groups.
When applying the configuration to Fortigate, all dependencies must be created first. 


Below is the order in which they should be created:

Configuration Steps:

Create Zones in Fortigate manually, as Zones are always created manually.
    Address
    Address Groups
    Address present in the Destination
    Services
    Policy
    Static Routes


Step 1:
The first step is to extract all the necessary files (Excel files) from the Palo Alto firewall. These include Addresses, Address Groups, and Addresses present in the Destination and Source fields.

Step 2:
Run the script provided in the respective files in the same order. Please note that you may need to modify some scripts based on text and other formats, but the overall idea remains the same.

Basic Understanding of Firewall Configuration in CLI:
To configure the firewall policy:


config firewall policy
    edit 1
        set name "Name"
        set srcintf "Name"
        set dstintf "Name"
        set action accept
        set srcaddr "NameOfAddress"
        set dstaddr "NameOfAddress"
        set schedule "always"
        set service "NameOfServices"
    next
The above will create a basic firewall policy structure. For more complex configurations, you'll need to use the full configuration.

Configuring Other Structures:
For Services:

config firewall service custom
    edit "ALL"
        set category "General"
        set protocol IP
    next
    edit "FTP"
        set category "File Access"
        set tcp-portrange 21
For Address:

config firewall address
    edit "0.0.0.0/16"
        set subnet 0.0.0.0/16
    next