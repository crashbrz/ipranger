import ipaddress
import sys

def generate_ip_range(ip_range, filename=None):
    # Create an ipaddress object
    ip_net = ipaddress.ip_network(ip_range, strict=False)

    # Generate a list of IP addresses in the network range
    ip_list = [str(ip) for ip in ip_net]

    # Print the list of IP addresses
    print("IP Address Range List")
    for ip in ip_list:
        print(ip)

    # Savethe IP addresses to a file
    if filename:
        with open(filename, 'w') as f:
            f.write('\n'.join(ip_list))
            print(f"IP list saved to {filename}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python ipranger.py <ip_range> <filename>")
        print("If you don't provide the filename, ipranger will display the IP list but not save it.")
        sys.exit(1)

    ip_range = sys.argv[1]
    filename = None
    if len(sys.argv) == 3:
        filename = sys.argv[2]

    generate_ip_range(ip_range, filename)
