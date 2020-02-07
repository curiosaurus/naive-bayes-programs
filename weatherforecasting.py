def get_freq(attributes,data,res=[]):
    freq={}
    nod=len(data)
    noa=len(attributes)
    if res!=[]:
        yes=res.count('Yes')
        no=res.count('no')
        proby=yes/nod
        probn=no/nod
    for i in range(noa):
        freq[attributes[i]]=0
        if (res!=[]):
            freq[attributes[i]+'_probablity']=0
            freq[attributes[i]+'_play']=0
            freq[attributes[i]+'_probablity_play']=0
    for j in range(nod):
        i=data[j]
        freq[i]+=1
        if (res!=[] and res[j]=='Yes'):
            freq[i+'_play']+=1
    if res!=[]:
        res.count('Yes')
        for i in range(noa):
            freq[attributes[i]+'_probablity']=freq[attributes[i]]/nod
            freq[attributes[i]+'_probablity_play']=freq[attributes[i]+'_play'] / yes
            freq['play_probablity_'+attributes[i]]=freq[attributes[i]+'_probablity_play']*proby/freq[attributes[i]+'_probablity']
    return freq
def get_prob():
    print("this is the get probability function")
weather=['Sunny','Sunny' ,'Overcast','Rain','Rain'  ,'Rain'  ,'Overcast','Sunny','Sunny' ,'Rain'  ,'Sunny' ,'Overcast','Overcast','Rain']
humidity=['High','High'  ,'High'    ,'High','Normal','Normal','Normal'  ,'High' ,'Normal','Normal','Normal','High'    ,'Normal'  ,'High']
wind=['Weak'    ,'Strong','Weak'    ,'Weak','Weak'  ,'Strong','Strong'  ,'Weak' ,'Weak'  ,'Weak'  ,'Strong','Strong'  ,'Weak'    ,'Strong']
play=['No'      ,'No'    ,'Yes'     ,'Yes' ,'Yes'   ,'No'    ,'Yes'     ,'No'   ,'Yes'   ,'Yes'   ,'Yes'   ,'Yes'     ,'Yes'     ,'No']
#print( len(weather), len(wind), len(humidity), len(play) )
freq_outlook=get_freq(['Sunny','Overcast','Rain'],weather,play)
freq_humid=get_freq(['High','Normal'],humidity,play)
freq_wind=get_freq(['Weak','Strong'],wind,play)
#freq_play=get_freq(['No','Yes'],play,play)
print(freq_outlook)
print('\n')
print(freq_humid)
print('\n')
print(freq_wind)
while True:
    w=input('What is outlook \n Sunny or Rain or Overcast : ')
    h=input('What is Humidity \n High or Normal : ')
    wi=input('How is wind\n Weak or Strong : ')
    likelihoody=0
    likelihoodn=0
    likelihoody=freq_outlook[w+'_probablity_play']*freq_humid[h+'_probablity_play']*freq_wind[wi+'_probablity_play']
    likelihoodn=(1-freq_outlook[w+'_probablity_play'])*(1-freq_humid[h+'_probablity_play'])*(1-freq_wind[wi+'_probablity_play'])
    print("Likelihood of play being yes:"+str(likelihoody)+'\nLikelihood of play being no:'+str(likelihoodn))
    print("Probability of play is :"+str(likelihoody/(likelihoody+likelihoodn)))
    ch=input('Enter 1 to Exit')
    if ch==1:
        break
#print(freq_play)