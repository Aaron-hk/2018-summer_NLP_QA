# encoding=utf-8

'''
模塊說明：
    運行文件
運行格式：
    python QA_main.py fileName scoreFile
參數說明：
    fileName：問答句測試集文件名
    scoreFile：得分輸出文件名
'''

import ReadFile
import ProcessData as ProD
import WordVec
import QueTypeWay
import sys



if __name__=="__main__":
    assert sys.argv.__len__()==3
    fileName=sys.argv[1]
    scoreFile=sys.argv[2]
    test=ReadFile.QAData(fileName)
    test.readFile()
    ProD.wordSeg(test)
    ProD.delHighFre_useless(test)
    ProD.delHighFre_psg(test)
    test.calFre()
    WordVec.writeScore1(test, scoreFile, "trainData.model")
    print("OK, DONE.")