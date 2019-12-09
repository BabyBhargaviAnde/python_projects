import requests
domain = "sviet.com"
file = open("subdomains.txt")
content = file.read()
subdomains = content.splitlines()
for subdomain in subdomains:
    url = "https://"+subdomain+"."+domain
    try:
        # if this raises an ERROR, that means the subdomain does not exist
        r = requests.get(url)
        if r.status_code ==200:
        	print(url)
        elif r.status_code ==301:
        	print(url)
        # print(url)net

    except:
        # if the subdomain does not exist, just pass, print nothing
        pass
    # else:
    #     print("[+] Discovered subdomain:",url)

# 200, 204, 301, 302, 401, 404, 500
