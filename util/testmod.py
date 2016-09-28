
import random

'''links:
http://www.bls.gov/oes/current/oes190000.htm
http://www.bls.gov/oes/current/oes110000.htm
http://www.bls.gov/oes/current/oes250000.htm
http://www.bls.gov/oes/current/oes230000.htm
http://www.bls.gov/oes/current/oes510000.htm
http://www.bls.gov/oes/current/oes390000.htm
http://www.bls.gov/oes/current/oes270000.htm
http://www.bls.gov/oes/current/oes450000.htm
http://www.bls.gov/oes/current/oes530000.htm
http://www.bls.gov/oes/current/oes130000.htm
http://www.bls.gov/oes/current/oes210000.htm
http://www.bls.gov/oes/current/oes470000.htm
http://www.bls.gov/oes/current/oes490000.htm
http://www.bls.gov/ooh/food-preparation-and-serving/home.htm
http://www.bls.gov/oes/current/oes370000.htm
http://www.bls.gov/ooh/architecture-and-engineering/home.htm
ttp://www.bls.gov/ooh/sales/home.htm
http://www.bls.gov/oes/current/oes330000.htm
http://www.bls.gov/oes/current/oes290000.htm
http://www.bls.gov/ooh/office-and-administrative-support/home.htm
http://www.bls.gov/oes/current/oes150000.htm
http://www.bls.gov/oes/current/oes310000.htm
'''
occupations = open('data/occupations.csv','r')
occupations = occupations.read()
occupations = occupations.split('\n')
occupations = occupations[1:len(occupations)-1] #removes the job class and the ttal
Occups = []
percentages = []
for x in range (0,len(occupations)-1):
    lastCom = occupations[x].rfind(",")
    y = occupations[x][:lastCom]#spliting a row into occupation adn percetage seerately
    if y.count(',')>0:#if there is more than one comma
        y = y[1:len(y)-1]#get rid of the ""
        #print y
    q = occupations[x][lastCom+1:]
   #print q
    Occups.append(y) #occupations is all the stuff before the last comma
    percentages.append(float(q)) #percent is after the last comma
    prof_dict = {}
for i in range(len(occupations)-1):#making it a dict
    prof_dict[Occups[i]] = percentages[i]
    
#for j in prof_dict:
#print j, prof_dict[j]

cumSum = {}#makin a dict  with cummulative percentages
yo = 0
for g in prof_dict:
    #print g
    #print prof_dict[g]
    cumSum[g] = prof_dict[g] + yo
    yo += prof_dict[g]
    #print cumSum['Life, Physical and Social Science']
cumLo = {}#makin a dict shifted one down from cumSum (1st place is 0)
yay = 0
for h in prof_dict:
    cumLo[h] = yay
    yay = cumSum[h]
    #print cumLo['Production']
   
def randMan():
    randNum = random.random() * 100
    
    for i in cumSum:
        if (cumSum[i] >= randNum) and (cumLo[i] < randNum):
            return i
        print i
        
