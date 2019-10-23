import re

text = []
with open('C:/Users/jerem/Desktop/MN_Translation/Mystic-Nights-Translation/SUBSYS.RES','rb') as data: #open file filename in read mode
    buffer = data.read()#read content

text = re.findall(b'\x20\x54\x45\x58\x54\x20\x22(.*)\x22', buffer, re.MULTILINE)
item_lists = re.findall(b'\x49\x54\x45\x4D\x5F\x4C\x49\x53\x54\x20\x22(.*)\x22', buffer, re.MULTILINE)
item_names = re.findall(b'\x4E\x41\x4D\x45\x20\x22(.*)\x22', buffer, re.MULTILINE)
item_desc = re.findall(b'\x44\x45\x53\x43\x52\x49\x50\x54\x49\x4F\x4E\x20\x22(.*)\x22', buffer, re.MULTILINE)
item_use = re.findall(b'\x55\x53\x45\x5F\x4D\x45\x53\x53\x41\x47\x45(.*)\x2E', buffer, re.MULTILINE)

print ("DECODING...")

for i in range(len(text)):
  text[i] = text[i].decode('euc-kr')
for i in range(len(item_lists)):
  item_lists[i] = item_lists[i].decode('euc-kr')
for i in range(len(item_names)):
  item_names[i] = item_names[i].decode('euc-kr')
for i in range(len(item_desc)):
  item_desc[i] = item_desc[i].decode('euc-kr')
for i in range(len(item_use)):
  item_use[i] = item_use[i].decode('euc-kr')

print("DECODING COMPLETE.\nEXPORTING TO LOGS...")

b'\x4E\x41\x4D\x45\x20\x22(.*)\x22'
with open('C:/Users/jerem/Desktop/MN_Translation/fulltext.txt', 'w', encoding='euc-kr') as f:
    for item in text:
        f.write("%s\n" % item)
with open('C:/Users/jerem/Desktop/MN_Translation/fullitems.txt', 'w', encoding='euc-kr') as f:
    for item in item_lists:
        f.write("ITEM LIST: ")
        f.write("%s\n" % item)
    for item in item_names:
        f.write("ITEM NAME: ")
        f.write("%s\n" % item)
    for item in item_desc:
        f.write("ITEM DESCRIPTION: ")
        f.write("%s\n" % item)
    for item in item_use:
        f.write("ITEM USE: ")
        f.write("%s\n" % item)
print("EXPORTING COMPLETE.")
