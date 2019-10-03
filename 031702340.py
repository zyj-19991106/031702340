
import re
import  cpca
import  json

while 1:
      inputraw=input();
      string1=inputraw
      if(inputraw=="END"):
         break

         typ=0
      if (string1[0:2]=='1!'):     #删去难度级
         string1 = string1.strip('1!')
         typ=1
      elif (string1[0:2]=='2!'):
         string1 = string1.strip('2!')
         typ=2
      else:
            string1 = string1.strip('3!')
            typ=2

      pattern1=re.compile(r'(.*),')
      pattern2=re.compile(r'\d{11}')
      name=pattern1.findall(string1) #提取名字
      phone=pattern2.findall(string1)  #提取电话


      list1=string1.split(str(name[0]))
      #print(list1)
      string2=list1[1]
      #print(string2)
      string2=string2.strip(',')
      string2=string2.strip('.')
      list2=string2.split(str(phone[0]))
      string3=list2[0]+list2[1]
      list3=string3.split()
      judge=list3[0][0:2]
      #print(judge)
      #print(list3)
      df=cpca.transform(list3,cut=False) #先用全文搜索划分一次，不行就用精确搜索
      arry1=df.values[0]
      #print(arry1[0])
      if (arry1[0][0:2]==''):  #判断省份是否为空，若不为空则继续判断
         change=1
      elif (arry1[0][0:2]!=judge):       #判断省份是否与judge相同，若相同则不需要转换搜索规则
         change=1
      else:
         change=0


      #print(change)
      if(change==1):
         df = cpca.transform(list3)
         arry1 = df.values[0]



      #关键字特判
      patternz=re.compile(r'(.+?)镇')
      patternj=re.compile(r'(.+?)街道')
      patternx=re.compile(r'(.+?)乡')
      patterns=re.compile(r'(.+?)苏木')
      patternms=re.compile(r'(.+?)南山区')

      stringt=str(arry1[3])   #取出需要划分的地址
      z=patternz.findall(stringt)
      j=patternj.findall(stringt)
      x=patternx.findall(stringt)
      s=patterns.findall(stringt)
      ms=patternms.findall(stringt)

      stringz=str(z)
      stringj=str(j)
      stringx=str(x)
      strings=str(s)
      stringms=str(ms)

      if (stringz!=('[]')):
         list4=stringt.split('镇')
         list4[0]+= '镇'
         Address=list(arry1)
         Address.pop()
         Address+=list4
      elif (stringj!=('[]')):
         list4 = stringt.split('街道')
         list4[0] += '街道'
         Address = list(arry1)
         Address.pop()
         Address += list4
      elif (stringx!=('[]')):
         list4 = stringt.split('乡')
         list4[0] += '乡'
         Address = list(arry1)
         Address.pop()
         Address += list4
      elif (strings!=('[]')):
         list4 = stringt.split('苏木')
         list4[0] += '苏木'
         Address = list(arry1)
         Address.pop()
         Address += list4
      elif (stringms!=('[]')):
         list4 = stringt.split('南山区')
         list4[0] += '南山区'
         Address = list(arry1)
         Address.pop()
         Address += list4
      else :
         Address = list(arry1)
         Address.insert(3, '')

      #print(Address)
      #直辖市特判
      if (Address[0]== '北京市'or '上海市'or '天津市' or '重庆市') :
         Address[0]=str(Address[0]).strip('市')


      pattern_j=re.compile(r'(.+?)街')
      pattern_x=re.compile(r'(.+?)巷')
      pattern_n=re.compile(r'(.+?)弄')
      pattern_ht=re.compile(r'(.+?)胡同')
      pattern_l=re.compile(r'(.+?)路')

      stringtt= str(Address[4])  # 取出需要7级划分的地址
      j1= pattern_j.findall(stringtt)
      x1= pattern_x.findall(stringtt)
      n1= pattern_n.findall(stringtt)
      ht1= pattern_ht.findall(stringtt)
      l1= pattern_l.findall(stringtt)

      stringz1 = str(j1)
      stringj1 = str(x1)
      stringx1 = str(n1)
      strings1 = str(ht1)
      stringms1 = str(l1)

      #街等行政级别特判
      if(typ==2):


         if (stringz1!= ('[]')):
            list6 = stringtt.split('街')
            list6[0] += '街'
            Address = list(arry1)
            Address[3]=Address[3].strip(list6[0]+list6[1])
            Address += list6
         elif (stringj1!= ('[]')):
            list6 = stringtt.split('巷')
            list6[0] += '巷'
            Address = list(arry1)
            Address[3]=Address[3].strip(list6[0]+list6[1])
            Address += list6
         elif (stringx1!= ('[]')):
            list6 = stringtt.split('弄')
            list6[0] += '弄'
            Address = list(arry1)
            Address[3]=Address[3].strip(list6[0]+list6[1])
            Address += list6
         elif (strings1!= ('[]')):
            list6 = stringtt.split('胡同')
            list6[0] += '胡同'
            Address = list(arry1)
            Address[3]=Address[3].strip(list6[0]+list6[1])
            Address += list6
         elif (stringms1!= ('[]')):
            list6 = stringtt.split('路')
            list6[0] += '路'
            Address = list(arry1)
            Address[3]=Address[3].strip(list6[0]+list6[1])
            Address += list6
         else:
            Address = list(arry1)
            Address.insert(3, '')
         pattern_no=re.compile(r'(.*)号')
         add_num=pattern_no.findall(Address[5])
         if (add_num==[]):
            Address.insert(5,'')
         else:
               add_num[0]+='号'
               Address[5]=Address[5].strip(add_num[0])
               Address.insert(5,add_num[0])




      dict1={'姓名':name[0],'手机':phone[0],'地址':Address}
      dict1=json.dumps(dict1,ensure_ascii=False)
      print(dict1)



