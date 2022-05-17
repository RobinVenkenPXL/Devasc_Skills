from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.10.164",
    port="22",
    username="admin",
    password="cisco"
    )
command = ["int loopback 3","ip address 2.2.2.2 255.255.255.0", "exit" ]
output=sshCli.send_config_set(command)
show=sshCli.send_command("show ip interface brief")
print(output)
print(show)
