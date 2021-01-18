'''
겨울이 되어 길거리 곳곳에서 붕어빵을 팔고 있다. 
성균이가 운영하는 붕어빵 가게 앞에는 NN명의 손님이 한 줄로 서 있다. 
각 손님은 a_i개의 붕어빵을 사려고 한다.

성균이는 같은 개수의 붕어빵을 구매 하는 손님들이 연속되어 있으면 담는 것이 더 수월하리라 생각한다. 
따라서 특정 손님을 정하고, 그 손님이 사려고 하는 붕어빵의 개수와 같은 개수의 붕어빵을 사려고 하는 손님들을 줄에서 모두 내보내려고 한다.

어떤 특정 개수의 붕어빵을 사려고 하는 사람들을 줄에서 내보내야, 같은 개수의 붕어빵을 사려고 하는 사람들이 연속된 구간 중 가장 긴 것의 길이가 최대가 되는지 구하는 프로그램을 작성하라.
'''
cnt = int(input()) #사람 수
cntList = [] #같은 수의 붕어빵을 사려고 하는 사람들이 연속된 수
numList = [] #붕어빵 수
cnt2 = 0 #새로운 배열의 길이
maxNum = 0
lineNum = 0
cntNum = 0
missNum = 0

for i in range(cnt) :
    num = int(input())
    if i == 0 :
        cntList.append(1)
        numList.append(num)
    elif num == numList[cnt2] :
        cntList[cnt2] += 1
    else :
        cntList.append(1)
        numList.append(num)
        cnt2 += 1    
    if cntList[cnt2] > maxNum :
        maxNum = cntList[cnt2]

for i in range(cnt2-1) :
    # print(maxNum)
    if numList[i] == numList[i+2] :
        missNum = numList[i+1]
        cntNum = numList[i]
        lineNum = cntList[i] + cntList[i+2]
        for j in range(i+3, cnt2+1) :
            if numList[j] == cntNum :
                lineNum += cntList[j]
            elif numList[j] == missNum :
                continue
            else :
                break
        if lineNum > maxNum :
            maxNum = lineNum

print(maxNum)