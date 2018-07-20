# encoding=utf-8


import ReadFile
import string
import ProcessData as ProD

'''
函數功能：
    將文本中的數字轉爲一個特定的詞語代替，提高句子相似度的檢驗
'''
def digitToSeg(qAData):
    segTarget = "多少"
    for qIndex in range(qAData.questionList.__len__()):
        for segIndex in range(qAData.questionList[qIndex].__len__()):
            for tmp in qAData.questionList[qIndex][segIndex]:
                if tmp in string.digits:
                    qAData.questionList[qIndex][segIndex] = segTarget
                    break
        for aIndex in qAData.qAnswersDic[qIndex].keys():
            for segIndex in range(qAData.qAnswersDic[qIndex][aIndex].__len__()):
                for tmp in qAData.qAnswersDic[qIndex][aIndex][segIndex]:
                    if tmp in string.digits:
                        qAData.qAnswersDic[qIndex][aIndex][segIndex] = segTarget
                        break


if __name__ == "__main__":
    test = ReadFile.QAData("training.data")
    test.readFile()
    ProD.wordSeg(test)
    ProD.delHighFre_useless(test)
    ProD.delHighFre_psg(test)
    digitToSeg(test)
    test.calFre()
    test.showQAData(100)
