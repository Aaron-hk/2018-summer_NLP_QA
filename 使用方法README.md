# 2018-summer_NLP_QA
made by：王陈阳，黄道龙，曹龙，覃艳美


请在本文件夹下运行该程序
程序运行格式：
          python QA_main.py 待测数据集文件 分数输出文件
参数说明：
  QA_main.py      主python文件
  待测数据集文件    需要测试的数据集
  分数输出文件      每个答句的得分输出文件

示例：
    python QA_main.py develop.data devScore.data



使用提供的评测程序可以评测得分的文件，得到MAP和ACC@1的评分数值。评测程序在evaluation文件夹下
格式示例：
    python evaluation/evaluation.py develop.data devScore.data result.log



FAQ：
  1、程序需要使用python的包如下：jieba，gensim，zhon。请根据提示安装需要的包
  2、如果文件输出路径出错，请在本文件夹下直接运行生成
  3、本机开发的python环境的运行版本为3.6
运行过程中如果遇到其他问题，请联系相关组员。谢谢
QQ聯繫： 2236146406  黃道龍  
        863457834   王陳陽



================================================================================
已經根據群里最新的調用要求進行修改，如遇到問題，請參考上述舊資料
updated 2018/07/24 8:08 AM
