import json
import cpca
import re
location=input()
if(location[0:2]=='1!'):
    flag=1
    location=location.strip('1!')
elif(location[0:2]=='2!'):
    flag=2
    location=location.strip('2!')
else:
    flag=3
    location=location.strip('3!')
#完成划分难度级

namepattern=re.compile(r'(.*),')
name=namepattern.findall(location)
#提取名字

phonepattern=re.compile(r'[0-9]{11}')
phone=phonepattern.findall(location)
#提取电话

listlocation=location.split(',')
location=listlocation[1]
listlocation=location.split(str(phone[0]))
location=listlocation[0]+listlocation[1]
#提取剩下的地址信息

location1=location.split()
dataframe=cpca.transform(location1,cut=False,lookahead=10)
listlocation=dataframe.values[0]
if(listlocation[0][0:2]!=location1[0][0:2]):
    dataframe=cpca.transform(location1,lookahead=10)
    listlocation = dataframe.values[0]
address=listlocation[-1]
listlocation=list(listlocation)
listlocation.pop()
if(listlocation[0]=='北京市'or'上海市'or'天津市'or'重庆市'):
    listlocation[0]=str(listlocation[0]).strip('市')
#提取完省，市，县/区
address=address.strip('.')
townpattern=re.compile(r'(.*?)镇')
town=townpattern.findall(address)
streetpattern=re.compile(r'(.*?)街道')
street=streetpattern.findall(address)
villagepattern=re.compile(r'(.*?)乡')
village=villagepattern.findall(address)
if(len(town)!=0):
    address=address.split('镇')
    address[0]+='镇'
    listlocation+=address
    address = address[1]
elif(len(street)!=0):
    address=address.split('街道')
    address[0]+='街道'
    listlocation+=address
    address = address[1]
elif(len(village)!=0):
    address=address.split('乡')
    address[0]+='乡'
    listlocation+=address
    address = address[1]
else:
    address=address.split()
    listlocation+=address
    listlocation.insert(3,'')
    address=address[0]
#提取完第四级地址
if(flag==2):
    listlocation.pop()
    print(address)
    road=re.search(r'(.*?港路)|(.*?[路街港道])|(.*胡同)|',address)
    if(road==None):
        listlocation.insert(4,'')
    else:
        road=road.group(0)
        road=road.split()
        listlocation+=road
        road=road[0]
        address=address.replace(road,'',1)
    number=re.search(r'(.*?[号弄])',address)
    if(number==None):
        listlocation.insert(5,'')
    else:
        number=number.group(0)
        number=number.split()
        listlocation+=number
        number=number[0]
        address=address.replace(number,'',1)
    if(len(address)!=0):
        address=address.split()
        listlocation+=address
    else:
        listlocation.insert(6,'')
#提取完7级地址
answer={'姓名':name[0],'手机':phone[0],'地址':listlocation}
answer=json.dumps(answer,ensure_ascii=False)
print(answer)


