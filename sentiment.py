from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')
text = "The intent behind the movie was great, but it could have been better"
text = 'it is so good'
fName = 'geocode1.txt'
rName = 'geocode1SentimentResultNew.txt'
#Neutral Positive Negative
def sentimentAnalysis(fileName,resultFileName):
    dic = {'positive':0,'negative':0,'neutral':0}
    with open(resultFileName,'w') as ff:
        with open(fileName,'r') as f:
            for i in f:
                try:
                    results = nlp.annotate(i,properties={
                            'annotators':'sentiment, ner, pos',
                            'outputFormat': 'json',
                            'timeout': 50000,
                            })
                    print(results["sentences"])
                    for s in results["sentences"]:
                        if s["sentiment"]=='Neutral':
                            dic['neutral']+=1
                        elif s["sentiment"]=='Negative':
                            dic['negative']+=1
                        else:
                            dic['positive']+=1
                        ff.write("{} : {}".format(" ".join(t["word"] for t in s["tokens"]),s["sentiment"])+'\n')
                        #print("{} : {}".format(" ".join(t["word"] for t in s["tokens"]),s["sentiment"]))
                except Exception:
                    continue
    print(dic)
sentimentAnalysis(fName,rName)
