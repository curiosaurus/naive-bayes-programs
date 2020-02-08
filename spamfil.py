import pprint
def get_freq(attributes,data,res=[]):
    freq={}
    nod=len(data)
    noa=len(attributes)
    if res!=[]:
        yes=res.count('spam')
        no=res.count('ham')
        proby=yes/nod
        probn=no/nod
    for i in range(noa):
        freq[attributes[i]]=0
        if (res!=[]):
            freq[attributes[i]+'_probablity']=0
            freq[attributes[i]+'_spam']=0
            freq[attributes[i]+'_probablity_spam']=0
    for j in range(nod):
        i=data[j]
        for k in range(noa):
          if attributes[k] in i:
            freq[attributes[k]]+=1
            if (res!=[] and res[j]=='spam'):
              freq[attributes[k]+'_spam']+=1
    if res!=[]:
        res.count('spam')
        for i in range(noa):
            freq[attributes[i]+'_probablity']=freq[attributes[i]]/nod
            freq[attributes[i]+'_probablity_spam']=freq[attributes[i]+'_spam'] / yes
            freq['spam_probablity_'+attributes[i]]=freq[attributes[i]+'_probablity_spam']*proby/freq[attributes[i]+'_probablity']
    return freq
pp = pprint.PrettyPrinter()

emails = ["Hii there I am inviting you to the party We will have fun. meet me at garden . see you",
"Happy Birthday We want party",
"Meet me in my cabin",
"Great party yesterday thanks for inviting",
"Glad to meet to today",
"Boys meet at the auditorium",
"Developers meet Pune 2020",
"party all night",
"Birthday party at my place",
"cool kids party you are invited",
"cricketers party 2020",
"coder meet",
"meet me at cafe",
"Party from me"]
result=["ham","spam","ham","ham","ham","ham","ham","spam","ham","spam","ham","spam","spam","spam"]
attributes=['party','meet']
freq=get_freq(attributes,emails,result)
pp.pprint(freq)
while True:
    attrt=[]
    w=input('Enter the mail: ')
    for i in attributes:
      attrt.append(0)
      if i in w:
        attrt[attributes.index(i)]=1
    likelihoody=0
    likelihoodn=0
    for i in range(len(attributes)):
      if attrt[i]==1:
        if likelihoody:
          likelihoody*=freq[attributes[i]+'_probablity_spam']
          likelihoodn*=(1-freq[attributes[i]+'_probablity_spam'])
        else:
          likelihoody=freq[attributes[i]+'_probablity_spam']
          likelihoodn=(1-freq[attributes[i]+'_probablity_spam'])
    print("Likelihood of spam being yes:"+str(likelihoody)+'\nLikelihood of spam being no:'+str(likelihoodn))
    print("Probability of spam is :"+str(100*(likelihoody/(likelihoody+likelihoodn))))
    ch=input('Enter 1 to Exit')
    if ch==1:
        break