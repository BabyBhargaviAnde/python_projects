from tldextract import extract

tsd, td, tsu = extract("https://blog.entersoftsecurity.com") # prints abc, hostname, com

url = td + '.' + tsu # will prints as hostname.com

print url