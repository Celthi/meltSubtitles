Melt subtitles(融化字幕)
====

只留具有生词的字幕，并给出生词的释义，[思路来源](https://zhuanlan.zhihu.com/p/25854872)

可以选择只保留生词和释义。

生词是是指词库以外的单词，所以每个人的生词库是不一样的，可以自己寻找适合自己的词库。
Introduction
====
Meltsubtitles take the subtitles *.srt in and spill out  new subtitles in which the English words that you already know will be removed and it will provide the meaning of the words you don't know.

思路
====
    1. 词库假定是你认识的单词 
    2. 将字幕里在词库中的单词去掉，
    3. 通过查询有道网页得到生词的释义
    4. 将释义加入到新的字幕文件中，
    5. done

效果
====
![原始](img/ori.jpg)
 
![给出生词释义](img/cn.jpg)

![二刷](img/sec.jpg)

安装和使用
====
0. 安装python 2.7.9 以上，推荐[python 3.5](https://www.python.org/downloads/release/python-353)
1. pip install -r requirements.txt 
2. python main.py zimu.srt


    如果指定单词库，单词库在文件夹wordsRepo, 加上"-w wordsRepo/文件", 默认使用5000的。
    
    如果指定文件夹,命令行加上"--path 文件夹"
   
    或者对多个字幕转换 python main.py *.srt 
   
    如果希望是英文释义，在命令行加上 "-e"
    
    如果是二刷，在命令行加上 "-2"

词库有[5000](http://www.wordfrequency.info/free.asp),[10000](https://github.com/first20hours/google-10000-english)
====


To do 
====
1. [x] 英文释义选择

2. [x] 批量转换

3. [ ] 可以放到一个网页，使用的人可以不用安装python，只需上传下载。
4. [ ] 可以用map函数式的思想减少for的使用
5. [ ] 如果有人需要，可以打包成exe，这样就不用安装Python。
5. [ ] 如果有需要，可以将生词导出到一个文件中，用于以后记忆，或者导入查词软件，比如有道的单词本里，用于自己日后复习。
