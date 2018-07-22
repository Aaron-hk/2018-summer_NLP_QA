# -*- encoding:UTF-8 -*-

'''
模塊說明：
    預處理數據函數模塊
'''

import string
import jieba
import re
from zhon import hanzi
import ReadFile



'''
函數功能：    
    分詞，使用網上開源的結巴分詞
'''
def wordSeg(qAData):
    puncList = string.punctuation + hanzi.punctuation
    for i in range(qAData.questionList.__len__()):
        qTmp = jieba.cut(qAData.questionList[i], HMM=True)
        qTarget = ""
        for tmp in qTmp:
            if tmp not in puncList:
                qTarget += (tmp + " ")
        qAData.questionList[i] = re.sub(u'([" "])+', r"\1", qTarget).split(" ")[:-1]
        for aIndex in qAData.qAnswersDic[i].keys():
            aTmp = jieba.cut(qAData.qAnswersDic[i][aIndex], HMM=True)
            aTarget = ""
            for tmp in aTmp:
                if tmp not in puncList:
                    aTarget += (tmp + " ")
            qAData.qAnswersDic[i][aIndex] = re.sub(u'([" "])+', r"\1", aTarget).split(" ")[:-1]



'''
函數功能：
    去掉無用詞及停用詞
'''
def delHighFre_useless(qAData):
    uselessWordList = ["知道", "我", "请问", "好奇", "你", "很"]
    highFreWordList = ["是"]
    stopWordList = ["的", "了"]
    delWordList = uselessWordList + highFreWordList + stopWordList
    for qIndex in range(qAData.questionList.__len__()):
        qTarget = []
        for seg in qAData.questionList[qIndex]:
            if seg not in delWordList:
                qTarget.append(seg)
        qAData.questionList[qIndex] = qTarget
        # '''
        for aIndex in qAData.qAnswersDic[qIndex].keys():
            aTarget = []
            for seg in qAData.qAnswersDic[qIndex][aIndex]:
                if seg not in delWordList:
                    aTarget.append(seg)
            qAData.qAnswersDic[qIndex][aIndex] = aTarget
        # '''



'''
函數功能：
    去掉文章中高頻詞語
'''
def delHighFre_psg(qAData):
    highFreThres = 5
    for qIndex in range(qAData.questionList.__len__()):
        queSegFre = {}
        for seg in qAData.questionList[qIndex]:
            queSegFre[seg] = 0
            for aIndex in qAData.qAnswersDic[qIndex].keys():
                if seg in qAData.qAnswersDic[qIndex][aIndex]:
                    queSegFre[seg] += 1
            if queSegFre[seg] > highFreThres:
                qAData.questionList[qIndex].remove(seg)
                for aIndex in qAData.qAnswersDic[qIndex].keys():
                    while (True):
                        if seg in qAData.qAnswersDic[qIndex][aIndex]:
                            qAData.qAnswersDic[qIndex][aIndex].remove(seg)
                        else:
                            break



if __name__ == "__main__":
    test = ReadFile.QAData("training.data")
    test.readFile()
    wordSeg(test)
    delHighFre_useless(test)
    delHighFre_psg(test)
    test.showQAData(num=100)
