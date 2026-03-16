import re
import ipaddress
def match_ip_rule(filepath1, filepath2):
    
    try:
        pattern = r"\d+\.\d+\.\d+\.\d+/?\d{0,2}"
        pattern2 = r"(ALLOW|DENY)"
        with open(filepath1, "r") as file1:
            for line1 in file1:
                ip_input = ipaddress.IPv4Address(line1.replace("\n",""))
                with open(filepath2, "r") as file2:
                    for line2 in file2:
                        mobj = "".join(re.findall(pattern, line2))
                        action = "".join(re.findall(pattern2, line2))
                        if '/' in mobj:
                            network = ipaddress.IPv4Network(mobj)
                            for host in network.hosts():
                                    if host == ip_input:
                                        print(f"{ip_input} : {action}")
                                        break
                        else:
                            ip = ipaddress.IPv4Address(mobj)
                            if ip == ip_input:
                                print(f"{ip_input} : {action}")
                                break
    
    except Exception as e:
        print(f"Exception caught is: {e}")


if __name__ == "__main__":
    filepath1 = "ip_list.txt"
    filepath2 = "fw_rules.txt"
    result = match_ip_rule(filepath1,filepath2)