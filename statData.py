# encoding=utf-8


import math
import os
import ReadFile
import ProcessData as ProD


uselessWordList=["知道", "我", "请问", "好奇", "你", "很"]
highFreWordList=["是"]
stopWordList=["的", "了"]
freThres=0.0002


'''
函數功能：
    刪除之前的文件
'''
def delFile(fileName):
    try:
        os.remove(fileName)
    except:
        pass



'''
函數功能：
    寫分析的結果到文本文件中
'''
def writeFile(fileName, rst):
    with open(fileName, "a", encoding="utf-8") as outFile:
        for tmp in rst:
            outFile.write(str(tmp))
            outFile.write("\t\t\t")
        outFile.write("\n")


'''
函數功能：
    查找問答句之間切分的大小範圍
'''
def findScope(qAData):
    rst=float(0)
    maxNum=float(0)
    for scope in range(1,10):
        num=float(0)
        for qIndex in range(qAData.questionList.__len__()):
            a=qAData.questionList[qIndex]
            if len(a)<scope:
                pass
            else:
                a=a[-scope:]
            b=qAData.qAnswersDic[qIndex][0]
            for seg in a:
                if seg in b:
                    num+=1.0/len(b)
        num=num/(math.log(scope)+1.0)
        if num>maxNum:
            rst=scope
            maxNum=num
    return rst


'''
函數功能：
    計算訓練集中詞語的頻數
'''
def calSegFre(qAData, fileName):
    freDic={}
    for qIndex in range(qAData.questionList.__len__()):
        for tmp in qAData.questionList[qIndex]:
            if tmp not in freDic.keys():
                freDic[tmp]=1
            else:
                freDic[tmp]+=1
        #'''
        for aIndex in qAData.qAnswersDic[qIndex].keys():
            for tmp in qAData.qAnswersDic[qIndex][aIndex]:
                if tmp not in freDic.keys():
                    freDic[tmp]=1
                else:
                    freDic[tmp]+=1
        #'''
    delFile(fileName)
    for key, item in sorted(freDic.items(), key=lambda Item:Item[1], reverse=True):
        if (float(item)/freDic.__len__())>freThres:
            writeFile(fileName, [key, item])



'''
函數功能：
    計算訓練集中字的頻數
'''
def calWordFre(qAData, fileName):
    freDic = {}
    for qIndex in range(qAData.questionList.__len__()):
        for tmp in qAData.questionList[qIndex]:
            if tmp not in freDic.keys():
                freDic[tmp] = 1
            else:
                freDic[tmp] += 1
        # '''
        for aIndex in qAData.qAnswersDic[qIndex].keys():
            for tmp in qAData.qAnswersDic[qIndex][aIndex]:
                if tmp not in freDic.keys():
                    freDic[tmp] = 1
                else:
                    freDic[tmp] += 1
        # '''
    delFile(fileName)
    for key, item in sorted(freDic.items(), key=lambda Item: Item[1], reverse=True):
        if (float(item) / freDic.__len__()) > (freThres/10):
            writeFile(fileName, [key, item])



'''
函數功能：
    計算問答句之間的長度比例關係
'''
def statQueAns(qAData, fileName):
    lenDic = {}
    for qIndex in range(qAData.questionList.__len__()):
        queLen=len(qAData.questionList[qIndex])
        ansLen=len(qAData.qAnswersDic[qIndex][0])
        prop=float(queLen)/ansLen
        prop=float((int(prop*10))/10)
        if prop in lenDic.keys():
            lenDic[prop]+=1
        else:
            lenDic[prop]=1
    delFile(fileName)
    for key, item in sorted(lenDic.items(), key=lambda Item: Item[1], reverse=True):
        writeFile(fileName, [key, item])




if __name__=="__main__":
    dataFile="training.data"
    test=ReadFile.QAData(dataFile)
    test.readFile()
    calWordFre(test, "calWordFre.data")
    ProD.wordSeg(test)
    #test.showQAData(100)
    calSegFre(test, "calSegFre.data")
    statQueAns(test, "statQueAns.data")