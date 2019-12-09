import tldextract
ext = tldextract.extract('blog.entersoftsecurity.com')
print(ext.subdomain)