import json

with open("BigData_gameBook3.json",encoding='utf8') as f:
    js_data=json.load(f)
new_js_data={}

for element in js_data:
    for attribute in element.keys():
        if attribute not in new_js_data:
            new_js_data[attribute]={}
        for detail_key in element[attribute]:
            if detail_key not in new_js_data[attribute].keys():
                new_js_data[attribute][detail_key]={}
            #剔除不规范数据
            element[attribute][detail_key]=element[attribute][detail_key].lower()
            if detail_key=="电池容量":
                if element[attribute][detail_key].split('w')[0][0] >'9' or element[attribute][detail_key].split('w')[0][0] <'0':
                    continue
                batterySize=float(element[attribute][detail_key].split('w')[0])
                if batterySize > 1000:
                    break
                
                    
            if element[attribute][detail_key] not in new_js_data[attribute][detail_key].keys():
                new_js_data[attribute][detail_key][element[attribute][detail_key]]=1
            else:
                new_js_data[attribute][detail_key][element[attribute][detail_key]]+=1
        
new_js_data.pop("主体")
new_js_data.pop("机器规格")

analysis=json.dumps(new_js_data,ensure_ascii=False,indent=4)     
with open("gameBook_data_result.json","w",encoding="utf-8") as write_f:
    write_f.write(analysis)
