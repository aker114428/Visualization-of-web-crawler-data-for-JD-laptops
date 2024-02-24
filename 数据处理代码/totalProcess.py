import json

with open("BigData_gameBook3.json",encoding='utf8') as f:
    js_data=json.load(f)
new_js_data={}

for element in js_data:
    for attribute in element.keys():
        if attribute=="主体" or attribute=="机器规格":
            continue
        for detail_key in element[attribute]:
            if detail_key not in new_js_data.keys():
                new_js_data[detail_key]={}
            #剔除不规范数据
            element[attribute][detail_key]=element[attribute][detail_key].lower()
            if detail_key=="电池容量":
                if element[attribute][detail_key].split('w')[0][0] >'9' or element[attribute][detail_key].split('w')[0][0] <'0':
                    continue
                batterySize=float(element[attribute][detail_key].split('w')[0])
                if batterySize > 1000:
                    break    
            if detail_key=="净重含电池（kg）":
                if element[attribute][detail_key][0] >'9' or element[attribute][detail_key][0] <'0':
                    continue
                

            if element[attribute][detail_key] not in new_js_data[detail_key].keys():
                new_js_data[detail_key][element[attribute][detail_key]]=1
            else:
                new_js_data[detail_key][element[attribute][detail_key]]+=1
        
new_js_data.pop("机身尺寸（mm）")
analysis=json.dumps(new_js_data,ensure_ascii=False,indent=4)     
with open("gameBook_data_result.json","w",encoding="utf-8") as write_f:
    write_f.write(analysis)
