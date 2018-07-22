# -*-encoding:UTF-8-*-

'''
模塊說明：
    使用Word2Vec進行模型的訓練和計算句子得分
'''

import math
import ReadFile
import ProcessData as ProD
from gensim.models import Word2Vec

scope = 6


'''
函數功能：
    將整理後的問答集輸出到文本文件
'''

def writeSegList(QTA, fileName):
    with open(fileName, "w", encoding="UTF-8") as outFile:
        for i in range(QTA.questionList.__len__()):
            for tmp in QTA.questionList[i]:
                outFile.write(tmp + "\n")
            for aIndex in QTA.qAnswersDic[i].keys():
                for tmp in QTA.qAnswersDic[i][aIndex]:
                    outFile.write(tmp + "\n")




'''
函數功能：
    根據設定的公式計算得分
'''

def writeScore1(qAData, outFile, modelName):
    model = Word2Vec.load(modelName)
    with open(outFile, "w", encoding="UTF-8") as out:
        for qIndex in range(qAData.questionList.__len__()):
            a = qAData.questionList[qIndex]
            if len(a) > scope:
                a = a[-scope:]
            a_len = a.__len__()
            for aIndex in qAData.qAnswersDic[qIndex].keys():
                highScore = 0
                b = qAData.qAnswersDic[qIndex][aIndex]
                if b.__len__() > a_len:
                    for i in range(b.__len__() - a_len + 1):
                        b_tmp = b[i:i + a_len]
                        try:
                            score = model.n_similarity(a, b_tmp)
                        except:
                            score = 0
                        try:
                            weight = 1
                            for tmp in a:
                                if tmp in b_tmp:
                                    weight *= (-math.log(qAData.quesTFDic[qIndex][tmp] / qAData.quesTFDic[qIndex][0]))
                            score *= weight
                        except:
                            score *= 0.75
                        highScore = max(score, highScore)
                        # print(i, "\t", aIndex, "\t", score)
                        if abs(highScore) <= 0.000001:
                            for a_seg in a:
                                for b_seg in b_tmp:
                                    try:
                                        highScore = max(highScore, a.index(a_seg) * model.similarity(a_seg, b_seg))
                                    except:
                                        pass
                else:
                    b_tmp = b
                    try:
                        score = model.n_similarity(a, b_tmp)
                    except:
                        score = 0
                    try:
                        weight = 1
                        for tmp in a:
                            if tmp in b_tmp:
                                weight *= (-math.log(qAData.quesTFDic[qIndex][tmp] / qAData.quesTFDic[qIndex][0]))
                        score *= weight
                    except:
                        score *= 0.75
                    highScore = max(score, highScore)
                    # print(i, "\t", aIndex, "\t", score)
                    if abs(highScore) <= 0.000001:
                        for a_seg in a:
                            for b_seg in b_tmp:
                                try:
                                    highScore = max(highScore, a.index(a_seg) * model.similarity(a_seg, b_seg))
                                except:
                                    pass

                out.write(str(highScore))
                out.write("\n")




'''
函數功能：
    基於詞頻的相似度匹配
'''

def writeScore2(qAData, outFile):
    with open(outFile, "w", encoding="UTF-8") as out:
        for qIndex in range(qAData.questionList.__len__()):
            a = qAData.questionList[qIndex]
            if len(a) > scope:
                a = a[-scope:]
            a_len = a.__len__()
            a_score = 1
            for seg in a:
                a_score *= (-math.log(qAData.quesTFDic[qIndex][seg] / qAData.quesTFDic[qIndex][0]))
            a_score /= a_len
            for aIndex in qAData.qAnswersDic[qIndex].keys():
                highScore = 0
                b = qAData.qAnswersDic[qIndex][aIndex]
                if b.__len__() > a_len:
                    for i in range(b.__len__() - a_len + 1):
                        b_tmp = b[i:i + a_len]
                        b_score = 1
                        for seg in b_tmp:
                            b_score *= (-math.log(qAData.quesTFDic[qIndex][seg] / qAData.quesTFDic[qIndex][0]))
                        b_score /= (a_len+1)
                        score = float(1) / (abs(a_score - b_score)+1)
                        # print(a_score, "\t", str(1/(score+0.1)))
                        highScore = max(score, highScore)
                        # print(i, "\t", aIndex, "\t", score)
                else:
                    b_tmp = b
                    b_score = 1
                    for seg in b_tmp:
                        b_score *= (-math.log(qAData.quesTFDic[qIndex][seg] / qAData.quesTFDic[qIndex][0]))
                    b_score /= (b_tmp.__len__()+1)
                    score = float(1) / (abs(a_score - b_score)+1)
                    # print(a_score, "\t", str(1 / (score + 0.1)))
                    highScore = max(score, highScore)
                out.write(str(highScore))
                out.write("\n")



'''
function usage:
    test just
'''
def writeScore3(qAData, outFile, modelName):
    model = Word2Vec.load(modelName)
    with open(outFile, "w", encoding="UTF-8") as out:
        for qIndex in range(qAData.questionList.__len__()):
            a = qAData.questionList[qIndex]
            if len(a) > scope:
                a = a[-scope:]
            a_len = a.__len__()
            for aIndex in qAData.qAnswersDic[qIndex].keys():
                highScore = 0
                b = qAData.qAnswersDic[qIndex][aIndex]
                if b.__len__() > a_len:
                    for i in range(b.__len__() - a_len + 1):
                        b_tmp = b[i:i + a_len]
                        try:
                            score = model.n_similarity(a, b_tmp)
                        except:
                            score = 0
                        highScore = max(score, highScore)
                        # print(i, "\t", aIndex, "\t", score)
                else:
                    b_tmp = b
                    try:
                        score = model.n_similarity(a, b_tmp)
                    except:
                        score = 0
                    highScore = max(score, highScore)
                    # print(i, "\t", aIndex, "\t", score)

                out.write(str(highScore))
                out.write("\n")



'''
函數功能：
    訓練詞向量
'''

def trainModel(qAData, outFile):
    sentences = []
    for i in range(qAData.questionList.__len__()):
        sentences.append(qAData.questionList[i])
        for aIndex in qAData.qAnswersDic[i].keys():
            sentences.append(qAData.qAnswersDic[i][aIndex])
    model = Word2Vec(sentences, min_count=1, size=100, workers=4)
    model.save(outFile)





if __name__ == "__main__":
    # '''
    fileName = "trainData.model"
    test = ReadFile.QAData("training.data")
    test.readFile()

    ProD.wordSeg(test)
    ProD.delHighFre_useless(test)
    ProD.delHighFre_psg(test)
    test.calFre()
    trainModel(test, fileName)
    # '''

    # '''
    # print(model.most_similar("性格"))
    # writeScore1(test, "score.data", "trainData.model")
    # writeScore2(test,"score.data")
    # '''
