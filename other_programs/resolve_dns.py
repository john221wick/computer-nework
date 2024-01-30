import socket

def resolve_hostname(hostname):
    ip_address = socket.gethostbyname(hostname)
    return f"IP address for {hostname} is {ip_address}"


hostname = "facebook.com"
result = resolve_hostname(hostname)
print(result)
