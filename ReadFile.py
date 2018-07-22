# -*- encoding:UTF-8 -*-

'''
模塊說明：
    構建數據集的數據結構，方便後續的預處理和操作
'''

'''
類說明：
    問答集對應的數據結構
成員：
    fileName：問答集的文件名
    questionList：問題組成列表
    qAnswersDic:答句的數據結構
    qLabelsDic：答句的標籤的數據結構
    quesTFDic：每個問題文檔中的詞頻數據機構
'''


class QAData():
    def __init__(self, fileName):
        self.fileName = fileName
        self.questionList = []
        self.qAnswersDic = {}
        self.qLabelsDic = {}
        self.quesTFDic = {}

    '''
    函數說明：
        讀取問答集文件到數據對象
    '''

    def readFile(self):
        data = open(self.fileName, "r", encoding="UTF-8").readlines()
        lastQuestion = " "
        qIndex = -1
        aIndex = 0
        for line in data:
            segList = line.split("\t")
            if lastQuestion != segList[0]:
                qIndex += 1
                aIndex = 0
                lastQuestion = segList[0]
                self.qAnswersDic[qIndex] = {}
                self.qLabelsDic[qIndex] = {}
                self.questionList.append(lastQuestion)
            self.qAnswersDic[qIndex][aIndex] = segList[1]
            if (segList.__len__() == 3):
                self.qLabelsDic[qIndex][aIndex] = segList[2]
            aIndex += 1

    '''
    函數說明：
        計算基於本文檔的詞頻
    ps：
        self.quesTFDic[qIndex][0]   爲一個問答文檔的總詞數
    '''

    def calFre(self):
        self.quesTFDic = {}
        for qIndex in range(self.questionList.__len__()):
            self.quesTFDic[qIndex] = {}
            self.quesTFDic[qIndex][0] = 0
            for seg in self.questionList[qIndex]:
                self.quesTFDic[qIndex][0] += 1
                if seg not in self.quesTFDic[qIndex].keys():
                    self.quesTFDic[qIndex][seg] = 1
                else:
                    self.quesTFDic[qIndex][seg] += 1
            for aIndex in self.qAnswersDic[qIndex].keys():
                for seg in self.qAnswersDic[qIndex][aIndex]:
                    self.quesTFDic[qIndex][0] += 1
                    if seg not in self.quesTFDic[qIndex].keys():
                        self.quesTFDic[qIndex][seg] = 1
                    else:
                        self.quesTFDic[qIndex][seg] += 1

    '''
    函數功能：
        顯示問答集合
    '''

    def showQAData(self, num=0):
        assert num >= 0
        if num == 0:
            maxNum = self.questionList.__len__()
        else:
            maxNum = min(num, self.questionList.__len__())
        for i in range(maxNum):
            print("===============================\n")
            print(i, ":\t", self.questionList[i])
            for aIndex in self.qAnswersDic[i].keys():
                print(aIndex, ":\t", self.qAnswersDic[i][aIndex])


if __name__ == "__main__":
    QADT = QAData("develop.data")
    QADT.readFile()
    QADT.showQAData()
