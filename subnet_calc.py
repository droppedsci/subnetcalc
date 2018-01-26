network_block = "x.x.11.0/24" # network_block assignment type(str)
subnet_mask = 26 #subnet mask assignment type(int)

# Split the network block into IP addresses and network masks

ip_address = network_block.split("/")[0] # splits the network_block variable into ip address and CIDR notation. Assigns x.x.11.0 to variable
network_mask = int(network_block.split("/")[1]) # takes the CIDR notation from the network_block variable and gives it a new assignment and type
octets = ip_address.split(".") # takes the IP address and removes the period and separates it into ['x','x','11','0']

# Find the octets number for which subnet address needs to be calculated
# class A = 1 , class B = 2, Class C = 3

subnet_octet = network_mask /8  #new variable assignment. Takes network_mask(24) and divides it by 8. Result should be 3 

# Find out how many subnets for a given network mask and subnet mask
number_of_subnets = 2 ** (subnet_mask - network_mask) # 26 - 24 = 2 * 2 = 4


# Total numbers of IPs within a subnet
# host class for class A,B and C is 16,24,and 32.

host_class = (subnet_octet * 8) + 8 # 3*8 = 24 + 8 = 32 
number_of_ips_per_subnet = 2 ** (host_class - subnet_mask) # 2 to the 6th power. Multiply  by 2 = 32 * 2 = 64 ips per subnet

#Derive the subnet addresses
subnetwork_address = int(octets[subnet_octet]) # sets subnetwork_address to integer value of 0

for each_subnet in range(0,number_of_subnets):     #variables each_subnet and number_of_subnets in the function. Loop starts at 0 and ends at 4. There will be 4 subnets displayed 
    octets[subnet_octet] = str(subnetwork_address)  # sets octets[subnet_octect] to a string value of 0 and tells the for loop to only update the last octet in the IP 
    subnets = ".".join(octets) + "/" + str(subnet_mask) # joins the IP address with periods and adds the CIDR value when output is requested
    print subnets   # output requested and printed
    subnetwork_address += number_of_ips_per_subnet # sets up to display all subnets in the range starting at x.x.11.0


 
