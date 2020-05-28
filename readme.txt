
爬虫文件是main.py可以根据需要更改里面的坐标参数和关键词参数
结果保存为文本文件

先激活stanfordnlp server
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000

启动之后即可运行脚本，部分function需要更改参数
geocode1，geocode2，geocode3分别代表3个时区，三个时区分开分析生成对应的geocodeSentimentResult文件
对文本内容进行情感分析使用sentiment，会生成sentimentResult文件，
在原文本内容每条twitter后面加了neutral，positive，negative分析结果
打印其中的dic可以获取neutral，positive，negative的数量
分析结果如下
{'positive': 192, 'negative': 263, 'neutral': 1234}

情感分析结果和高频词汇结果都使用matplotlib的扇形图绘制，可以更改counter.py中的参数实现
example是其中的一个运行结果画的高频词统计图
如果想在网页上点击运行然后画图可以使用jupyternotebook