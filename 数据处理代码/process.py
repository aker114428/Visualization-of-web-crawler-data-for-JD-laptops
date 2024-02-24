import json

with open('processedThinkBookInfo.json',encoding='utf8') as f:
    gameBookInfo=json.load(f);

newGameBookInfo=dict()

for it in gameBookInfo.keys():
    newGameBookInfo[it]=dict()
    varieties=list()
    numlist=list()
    for key in gameBookInfo[it].keys():
        varieties.append(key)
        numlist.append(gameBookInfo[it][key])
    newGameBookInfo[it]["类别"]=varieties
    newGameBookInfo[it]["数量"]=numlist

analysis=json.dumps(newGameBookInfo,ensure_ascii=False,indent=4)  
with open("newThinkBookInfo.json","w",encoding="utf-8") as write_f:
    write_f.write(analysis)