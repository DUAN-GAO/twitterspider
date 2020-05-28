import matplotlib.pyplot as plt

def counter(fileName,num): #fileName是文件名 num是你想获取的高频词数量
    dic={}
    a = []
    b = []
    with open(fileName,'r') as f:
        for i in f:
            words = i.split()
            for word in words:
                if word in dic:
                    dic[word] += 1
                else:
                    dic[word] = 1
    f = zip(dic.values(),dic.keys())
    f = sorted(f)[-num:]
    #print(sorted(f)[-num:])
    for i in f:
        print(i)
        a.append(i[0])
        b.append(i[1])
    print(a)
    a = [i/sum(a) for i in a]
    plt.pie(a,labels=b,autopct="%.1f%%")
    plt.savefig('pie.png')
counter('result.txt',20)