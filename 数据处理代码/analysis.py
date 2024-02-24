import json

with open("BigData_gameBook3.json",encoding='utf8') as f:
    js_data=json.load(f)

""" #去重
newlist=[]
for i in js_data:
    if i not in newlist:
        newlist.append(i)
js_data=newlist """

#数据处理
cpuVarietyCount={}
for x in js_data:
    if "处理器" not in x.keys():
        continue
    cpuinfor=x["处理器"]
   
    keyname=''
    for k in cpuinfor.keys():
        if k.find('处理器品牌')!=-1:
            keyname=k
    if keyname=="":
        continue
    if cpuinfor[keyname] not in cpuVarietyCount.keys():
        cpuVarietyCount[cpuinfor[keyname]]=1
    else:
        cpuVarietyCount[cpuinfor[keyname]]+=1


#格式化数据和写文件
result={"游戏本处理器品牌和数量":cpuVarietyCount}
analysis=json.dumps(result,ensure_ascii=False,indent=4)     
print(type(analysis))
print(analysis)
with open("data_result.json","w",encoding="utf-8") as write_f:
    write_f.write(analysis)


