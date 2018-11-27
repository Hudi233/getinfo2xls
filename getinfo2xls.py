import json
import requests
import json
from bs4 import BeautifulSoup
import dicttoxml
import xlwt

xls = xlwt.Workbook()
sheet = xls.add_sheet('sheet',cell_overwrite_ok=True)
keyword = ['ips','department','business','owner','op_owner','cluster']
num = 0
for x in range(len(keyword)):
    sheet.write(0,num,keyword[x])
    num += 1
def getvalue(date):

    URL = CMDB_url
    headers = {
    'Content-Type': 'application/json',
    'username': 'username',
    'Authorization': 'password'
	}

    req = requests.post(url=URL,json=data,headers=headers)
#    global value 
    value = json.loads(req.text)
    return value


#从txt中读取IP输入data

f = open("iptest1.txt")
lines = f.readlines()
array = []

for line in lines:
    array.append(line)
f.close()


for i in range(len(array)):
    
#    print i

    data = {
         'ips': array[i].strip()
	}
#    print getvalue(data)
    result = getvalue(data)
    value = []  
    value.append(result)
#    print value
     
#json to xml
    xml = dicttoxml.dicttoxml(value)
#将关键字和转换后的xml的值写入xls
    soup = BeautifulSoup(xml,'html.parser')
    info_list = []
    for k in range(len(keyword)):
        for se in soup.find_all(keyword[k]):
#            print keyword
            info = se.get_text()
            info_list.append(info)
#           print se
#           print info_list
    numx = 0   
    for j in range(len(info_list)):
        sheet.write(i+1,numx,info_list[j])
        numx += 1

    
xls.save('test.xls')

jiedaibao
password
mysql
