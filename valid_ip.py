s="123.045.067.089"

def is_valid_IP(s):
    ips = [i for i in s.split(".")]
    valids = [i[0] != "0" and len(ips)==4 and i.isdigit() and 0 <= int(i) <= 255 for i in ips]
    return all(valids) == True      


print(is_valid_IP(s))



