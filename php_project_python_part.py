def win(curlist,curplayer):
    for i in range(0,9,3):
        if (curlist[i] == curplayer):
            if(curlist[i] == curlist[i+1]):
                if(curlist[i] == curlist[i+2]):
                    return True
    for i in range(3):
        if (curlist[i] == curplayer):
            if(curlist[i] == curlist[i+3]):
                if(curlist[i] == curlist[i+6]):
                    return True
    if (curlist[0] == curplayer):
        if(curlist[0] == curlist[4]):
            if(curlist[0] == curlist[8]):
                return True
    if (curlist[2] == curplayer):
        if(curlist[2] == curlist[4]):
            if(curlist[2] == curlist[6]):
                return True
    return False
statedict = {}
#FORMAT:
#store(str,str,str,int,statedict)
# int input can only be 0,1,-1 for tic-tac-toe 
def store(count,prevstate,curstate,reward,statedict):
    if str(statedict.keys()).find(str(count)) == -1: #count not found in memory
        statedict[count] = {prevstate:{curstate:reward}}
    else:
        dic2 = statedict[count]
        if str(dic2.keys()).find(prevstate) == -1: #prevstate not found in the memory
            dic2[prevstate] = {curstate:reward}
        else:
            dic3 = dic2[prevstate]
            if str(dic3.keys()).find(curstate) == -1: #curstate not found in the memory
                dic3[curstate] = reward
            else:
                temp = dic3[curstate]
                temp = reward + temp
                dic3[curstate] = temp
def printmat(curlist):
    for i in range(1,len(curlist)+1):
        if i%3 == 0:
            print(str(curlist[i-1])+'|')
        else:
            print(str(curlist[i-1])+'|',end='')
def randomfunc(curlist):
    while True:
        i = random.randint(0,8)
        if(curlist[i] == 0):
            return i
        else:
            pass
import random
def evenComp(count, prevstate, board): 
    r,e = predwin(board)
    if e:
        return r
    else:
        pass
    h = True
    while h:
        i = random.randint(0,8)
        if(board[i]==0):
            h = False
        else:
            pass
    if str(statedict.keys()).find(str(count)) == -1: #count not found in memory
        
        return i
    else:
        dic2 = statedict[count]
        if str(dic2.keys()).find(prevstate) == -1: #prevstate not found in the memory
            return i
        else:  
            temp_return = -1000
            num = "a"
            dic3 = dic2[prevstate]
            an_array = list(dic3.keys())
            for j in an_array:
                if(dic3[j]>temp_return):
                    temp_return = dic3[j]
                    num = j
                  #  print("temp_return",temp_return)
                else:
                    pass
           # print("I am Numb",num)
            if(num == "a"):
                return i
            else:
                if(board[int(num)]==0):
                    print("memory used")
                    return int(num)
                else:
                    return i;
def predwin(curlist):
    l = []
    for i in range(0,len(curlist)):
        if(curlist[i] == 0):
            l.append(i)
    for i in l:
        temp = curlist[:]
        temp[i] = 2
        m = win(temp,2)
        if m:
            return i,True
        temp[i] = 1
        m = win(temp,1)
        if m:
            return i,True
    return i,False
def gamestat(curlist,curplayer):
    cur = 0
    for i in range(0,9,3):
        if (curlist[i] == curplayer):
            if(curlist[i] == curlist[i+1]):
                if(curlist[i] == curlist[i+2]):
                    cur = cur + 1
    for i in range(3):
        if (curlist[i] == curplayer):
            if(curlist[i] == curlist[i+3]):
                if(curlist[i] == curlist[i+6]):
                    cur = cur + 1
    if (curlist[0] == curplayer):
        if(curlist[0] == curlist[4]):
            if(curlist[0] == curlist[8]):
                cur = cur + 1
    if (curlist[2] == curplayer):
        if(curlist[2] == curlist[4]):
            if(curlist[2] == curlist[6]):
                cur = cur + 1
    if(cur == 1):
        if(curplayer == 1):
            return -1
        else:
            return 2
    elif(cur>1):
        if(curplayer == 1):
            return -10
        else:
            return 20
    else:
        print("Something is wrong with gamestat")
        return 0

import pandas as pd
colnames=['count', 'prev', 'cur', 'rew'] 
user1 = pd.read_csv('nested_dict1.csv', names=colnames, header=None)
statedict = {}
for i in range(0,len(user1)):
    store(str(user1["count"][i]),str(user1["prev"][i]),str(user1["cur"][i]),int(user1["rew"][i]),statedict)
count = 0
winbool = False
curlist = [0,0,0,0,0,0,0,0,0]
cur = 1
other = 2
curstate = None
t = True
Prevmove = None
Overall = []
while t:
    print("_____________")
    print("Move :",count)
    a = None
    h = True
    while h:
        try:
            if cur == 1:
                a= int(input())
            else:
                a = evenComp(str(count+1),str(Prevmove),curlist)
            if curlist[a] == 0:
                if cur == 2:
                    curlist[a] = cur
                    curstate = a
                    printmat(curlist)
                else:
                    curlist[a] = cur
                    printmat(curlist)
            else:
                h = True
                print("Already filled ")
                continue
            count = count + 1
            h = False
        except:
            t = False
            print("Incorrect input sorry ")
            break
            print("Enter again : ")
    print("Player :",cur)
    winbool = win(curlist,cur)
    if winbool == True:
        print(str(cur)+ "  WINS!!!")
        temp_num1 = 0
        if(cur == 1):
            temp_num1 = gamestat(curlist,cur)
        else:
            temp_num1 = gamestat(curlist,cur)
        for i in range(0,len(Overall)):
            store(str(Overall[i][0]),str(Overall[i][1]),str(Overall[i][2]),temp_num1,statedict)
        break
    else:
        if(cur == 2):
            edge = [1,3,5,7]
            diag = [0,2,6,8]
            center = [4]
            Temp_prevmove = -1
            if Prevmove in diag:
                Temp_prevmove = diag
            elif Prevmove in edge:
                Temp_prevmove = edge
            else:
                Temp_prevmove = center
            Temp_curstate = -1
            if curstate in diag:
                Temp_curstate = diag
            elif curstate in edge:
                Temp_curstate = edge
            else:
                Temp_curstate = center
            
            for qwe in Temp_prevmove:
                for qwe1 in Temp_curstate:
                    Overall.append([count,qwe,qwe1])
        pass
    curstr = str(curlist)
    if curstr.find('0') == -1:
        print('Draw')
        printmat(curlist)
        break
    else:
        Prevmove = a
        if(cur == 1):
            cur = 2
            other = 1
        else:
            cur = 1
            other = 2
print(" The game is over ")
