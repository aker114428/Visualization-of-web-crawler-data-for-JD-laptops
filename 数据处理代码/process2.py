import json

with open('gameBook_data_result.json',encoding='utf8') as f:
    gameBookInfo=json.load(f);

newButteryInfo=dict()
newButteryInfo["小于40wh"]=0
newButteryInfo["40-50wh"]=0
newButteryInfo["50-60wh"]=0
newButteryInfo["60-70wh"]=0
newButteryInfo["70-80wh"]=0
newButteryInfo["大于80wh"]=0

for val in gameBookInfo["电池容量"].keys():
    value=float(val.split('wh')[0])
    if value<40:
        newButteryInfo["小于40wh"]+=gameBookInfo["电池容量"][val]
    elif value>=40 and value<50:
        newButteryInfo["40-50wh"]+=gameBookInfo["电池容量"][val]
    elif value>=50 and value<60:
        newButteryInfo["50-60wh"]+=gameBookInfo["电池容量"][val]
    elif value>=60 and value<70:
        newButteryInfo["60-70wh"]+=gameBookInfo["电池容量"][val]
    elif value>=70 and value<80:
        newButteryInfo["70-80wh"]+=gameBookInfo["电池容量"][val]
    elif value>=80:
        newButteryInfo["大于80wh"]+=gameBookInfo["电池容量"][val]

gameBookInfo["电池容量"]=newButteryInfo

screenSize=dict()
screenSize["小于10英寸"]=0
screenSize["10-10.9英寸"]=0
screenSize["11-11.9英寸"]=0
screenSize["12-12.9英寸"]=0
screenSize["13-13.9英寸"]=0
screenSize["14-14.9英寸"]=0
screenSize["15-15.9英寸"]=0
screenSize["16-16.9英寸"]=0
screenSize["17-17.9英寸"]=0
screenSize["大于18英寸"]=0

for val in gameBookInfo["屏幕尺寸"].keys():
    value=float(val.split('英寸')[0])
    if value<10:
        screenSize["小于10英寸"]+=gameBookInfo["屏幕尺寸"][val]
    elif value>=10 and value<=10.9:
        screenSize["10-10.9英寸"]+=gameBookInfo["屏幕尺寸"][val]
    elif value>=11 and value<=11.9:
        screenSize["11-11.9英寸"]+=gameBookInfo["屏幕尺寸"][val]
    elif value>=12 and value<12.9:
        screenSize["12-12.9英寸"]+=gameBookInfo["屏幕尺寸"][val]
    elif value>=13 and value<=13.9:
        screenSize["13-13.9英寸"]+=gameBookInfo["屏幕尺寸"][val]
    elif value>=14 and value<=14.9:
        screenSize["14-14.9英寸"]+=gameBookInfo["屏幕尺寸"][val]
    elif value>=15 and value<=15.9:
        screenSize["15-15.9英寸"]+=gameBookInfo["屏幕尺寸"][val]
    elif value>=16 and value<16.9:
        screenSize["16-16.9英寸"]+=gameBookInfo["屏幕尺寸"][val]
    elif value>=17 and value<=17.9:
        screenSize["17-17.9英寸"]+=gameBookInfo["屏幕尺寸"][val]
    elif value>=18:
        screenSize["大于18英寸"]+=gameBookInfo["屏幕尺寸"][val]

gameBookInfo["屏幕尺寸"]=screenSize

#处理器加速频率
CPUFrequency=dict()
CPUFrequency["小于2ghz"]=0
CPUFrequency["2-2.5ghz"]=0
CPUFrequency["2.5-2.9ghz"]=0
CPUFrequency["3-3.5ghz"]=0
CPUFrequency["3.5-3.9ghz"]=0
CPUFrequency["4-4.5ghz"]=0
CPUFrequency["4.5-4.9ghz"]=0
CPUFrequency["大于5ghz"]=0

for val in gameBookInfo["处理器加速频率"].keys():
    value=float(val.split('ghz')[0])
    if value<2:
        CPUFrequency["小于2ghz"]+=gameBookInfo["处理器加速频率"][val]
    elif value>=2 and value<2.5:
        CPUFrequency["2-2.5ghz"]+=gameBookInfo["处理器加速频率"][val]
    elif value>=2.5 and value<=2.9:
        CPUFrequency["2.5-2.9ghz"]+=gameBookInfo["处理器加速频率"][val]
    elif value>=3 and value<3.5:
        CPUFrequency["3-3.5ghz"]+=gameBookInfo["处理器加速频率"][val]
    elif value>=3.5 and value<=3.9:
        CPUFrequency["3.5-3.9ghz"]+=gameBookInfo["处理器加速频率"][val]
    elif value>=4 and value<4.5:
        CPUFrequency["4-4.5ghz"]+=gameBookInfo["处理器加速频率"][val]
    elif value>=4.5 and value<=4.9:
        CPUFrequency["4.5-4.9ghz"]+=gameBookInfo["处理器加速频率"][val]
    elif value>=5:
        CPUFrequency["大于5ghz"]+=gameBookInfo["处理器加速频率"][val]

gameBookInfo["处理器加速频率"]=CPUFrequency

#处理器基准频率
CPUFrequency=dict()
CPUFrequency["小于1ghz"]=0
CPUFrequency["1-1.5ghz"]=0
CPUFrequency["1.5-1.9ghz"]=0
CPUFrequency["2-2.5ghz"]=0
CPUFrequency["2.5-2.9ghz"]=0
CPUFrequency["3-3.5ghz"]=0
CPUFrequency["3.5-3.9ghz"]=0
CPUFrequency["大于4ghz"]=0

for val in gameBookInfo["处理器基准频率"].keys():
    value=float(val.split('ghz')[0])
    if value<1:
        CPUFrequency["小于1ghz"]+=gameBookInfo["处理器基准频率"][val]
    elif value>=1 and value<1.5:
        CPUFrequency["1-1.5ghz"]+=gameBookInfo["处理器基准频率"][val]
    elif value>=1.5 and value<=1.9:
        CPUFrequency["1.5-1.9ghz"]+=gameBookInfo["处理器基准频率"][val]
    elif value>=2 and value<2.5:
        CPUFrequency["2-2.5ghz"]+=gameBookInfo["处理器基准频率"][val]
    elif value>=2.5 and value<=2.9:
        CPUFrequency["2.5-2.9ghz"]+=gameBookInfo["处理器基准频率"][val]
    elif value>=3 and value<3.5:
        CPUFrequency["3-3.5ghz"]+=gameBookInfo["处理器基准频率"][val]
    elif value>=3.5 and value<=3.9:
        CPUFrequency["3.5-3.9ghz"]+=gameBookInfo["处理器基准频率"][val]
    elif value>=4:
        CPUFrequency["大于4ghz"]+=gameBookInfo["处理器基准频率"][val]

gameBookInfo["处理器基准频率"]=CPUFrequency

#游戏本净重处理

pureWeight=dict()
pureWeight["小于1kg"]=0
pureWeight["1-1.5kg"]=0
pureWeight["1.5-1.9kg"]=0
pureWeight["2-2.5kg"]=0
pureWeight["2.5-2.9kg"]=0
pureWeight["3-3.5kg"]=0
pureWeight["3.5-3.9kg"]=0
pureWeight["大于4kg"]=0

for val in gameBookInfo["净重含电池（kg）"].keys():
    value=float(val)
    if value<1:
        pureWeight["小于1kg"]+=gameBookInfo["净重含电池（kg）"][val]
    elif value>=1 and value<1.5:
        pureWeight["1-1.5kg"]+=gameBookInfo["净重含电池（kg）"][val]
    elif value>=1.5 and value<=1.9:
        pureWeight["1.5-1.9kg"]+=gameBookInfo["净重含电池（kg）"][val]
    elif value>=2 and value<2.5:
        pureWeight["2-2.5kg"]+=gameBookInfo["净重含电池（kg）"][val]
    elif value>=2.5 and value<=2.9:
        pureWeight["2.5-2.9kg"]+=gameBookInfo["净重含电池（kg）"][val]
    elif value>=3 and value<3.5:
        pureWeight["3-3.5kg"]+=gameBookInfo["净重含电池（kg）"][val]
    elif value>=3.5 and value<=3.9:
        pureWeight["3.5-3.9kg"]+=gameBookInfo["净重含电池（kg）"][val]
    elif value>=4:
        pureWeight["大于4kg"]+=gameBookInfo["净重含电池（kg）"][val]

gameBookInfo["净重含电池（kg）"]=pureWeight

#轻薄本净重处理
""" 
pureWeight=dict()
pureWeight["0-0.5kg"]=0
pureWeight["0.5-0.9kg"]=0
pureWeight["1-1.5kg"]=0
pureWeight["1.5-1.9kg"]=0
pureWeight["2-2.5kg"]=0
pureWeight["2.5-2.9kg"]=0
pureWeight["大于3kg"]=0

for val in gameBookInfo["产品净重（kg）"].keys():
    value=float(val)
    if value>=0 and value<0.5:
        pureWeight["0-0.5kg"]+=gameBookInfo["产品净重（kg）"][val]
    elif value>=0.5 and value<1:
        pureWeight["0.5-0.9kg"]+=gameBookInfo["产品净重（kg）"][val]
    elif value>=1 and value<1.5:
        pureWeight["1-1.5kg"]+=gameBookInfo["产品净重（kg）"][val]
    elif value>=1.5 and value<2:
        pureWeight["1.5-1.9kg"]+=gameBookInfo["产品净重（kg）"][val]
    elif value>=2 and value<2.5:
        pureWeight["2-2.5kg"]+=gameBookInfo["产品净重（kg）"][val]
    elif value>=2.5 and value<3:
        pureWeight["2.5-2.9kg"]+=gameBookInfo["产品净重（kg）"][val]
    elif value>=3 :
        pureWeight["大于3kg"]+=gameBookInfo["产品净重（kg）"][val]

gameBookInfo["产品净重（kg）"]=pureWeight """

analysis=json.dumps(gameBookInfo,ensure_ascii=False,indent=4)  
with open("processedGameBookInfo.json","w",encoding="utf-8") as write_f:
    write_f.write(analysis)