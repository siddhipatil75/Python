
def update_allowed_ips(allowed_ips):
    print("\nEnter the IP addresses to add (type 'done' to stop):")
    while True:
        ip = input("Enter IP: ")
        if ip.lower() == "done":
            break
        allowed_ips.append(ip)
    return allowed_ips


def display_config(server_ip, allowed_ips):
    print("\n=== Server Configuration ===")
    print(f"Server IP (cannot be changed): {server_ip[0]}")
    print(f"Allowed IPs: {allowed_ips}")


print(" Web Server Configuration System ")


server_ip_input = input("Enter the server IP address: ")
server_ip = (server_ip_input,)  


allowed_ips = []
n = int(input("How many allowed IPs to enter initially? "))
for i in range(n):
    ip = input(f"Enter allowed IP {i+1}: ")
    allowed_ips.append(ip)


while True:
    print("\n MENU ")
    print("1. View Configuration")
    print("2. Update Allowed IPs")
    print("3. Try to Change Server IP (Not Allowed)")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        display_config(server_ip, allowed_ips)
    elif choice == "2":
        allowed_ips = update_allowed_ips(allowed_ips)
    elif choice == "3":
        print("\n Server IP cannot be changed! It's stored as a tuple (immutable).")
    elif choice == "4":
        print("\nExiting... Goodbye!")
        break
    else:
        print("\nInvalid choice! Please select a valid option.")
        
        
        
