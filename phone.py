import re
text = "If you want to call me, my old number was 8705343211 and it has been changed to 289-544-2345"
phone = re.findall('^[789]\d{9}$',text)

for call in phone:
	print (call[0])