# encoding=utf-8

import ReadFile

'''
函數功能：
    讀取分數文件，得到分數的數據對象
'''
def readScores(qAData, scoreFile):
    scoreDic = {}
    with open(scoreFile, mode="r", encoding="utf-8") as scf:
        scoresList = scf.readlines()
    for qIndex in range(qAData.questionList.__len__()):
        ansNum = len(qAData.qAnswersDic[qIndex])
        scoreDic[qIndex] = {}
        for i in range(ansNum):
            scoreDic[qIndex][i] = scoresList.pop(0)
    return scoreDic


'''
函數功能：
    展示錯誤的實例
'''
def showErr(qAData, scoreDic, Num):
    showNum = 0
    for qIndex in range(len(scoreDic)):
        highscore = float(scoreDic[qIndex][0])
        flag = 1
        for i in range(1, len(scoreDic[qIndex])):
            if highscore < float(scoreDic[qIndex][i]):
                flag = 0
                showNum += 1
                print("\n\n=========================================")
                print(qAData.questionList[qIndex])
                print(qAData.qAnswersDic[qIndex][0], "\t", scoreDic[qIndex][0])
                print(qAData.qAnswersDic[qIndex][i], "\t", scoreDic[qIndex][i])
                break
        '''
        if flag==0:
            print("\n\n=========================================")
            print(qAData.questionList[qIndex])
            for aIndex in range(len(scoreDic[qIndex])):
                print(qAData.qAnswersDic[qIndex][aIndex], "\t", scoreDic[qIndex][aIndex])
        '''
        if showNum >= Num:
            break


if __name__ == "__main__":
    test = ReadFile.QAData("training.data")
    test.readFile()
    scoreDic = readScores(test, "score.data")
    showErr(test, scoreDic, 100)
