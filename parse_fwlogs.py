import re

def parse_file(filepath):
    
    ip_data = {}
    ip_list = []
    pattern1 = r"DENY src=\d+\.\d+\.\d+\.\d+"
    pattern2 = r"\d+\.\d+\.\d+\.\d+"
    
    try:
        with open(filepath, "r") as file:
            for line in file:
                mstr = "".join(re.findall(pattern1, line))
                if mstr:
                    mip = "".join(re.findall(pattern2, mstr))
                    count = ip_data.get(mip)
                    if count is None:
                        ip_data[mip] = 1
                    else:
                        count += 1
                        ip_data[mip] = count
        for i in ip_data:
            if ip_data[i] > 5:
                ip_list.append(i)
        
        return ip_list        
                    
        
    except Exception as e:
        print(f"The exception occured is: {e}")
        
    return ip_list


if __name__ == "__main__":
    filepath = "firewall_logs.txt"
    result = parse_file(filepath)
    print(f"The IPs having DENY more than 5 is: {result}")