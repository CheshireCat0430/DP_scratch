memberNum, connectNum = map(int, input().split())
money = []
memberConnect = []
result = True

for i in range(memberNum) :
    num = int(input())
    money.append(num)
    memberConnect.append(i)

for i in range(connectNum) :
    a, b = map(int, input().split())
    mem1 = a
    mem2 = b
    for i in range(connectNum) :
        if memberConnect[mem1] != mem1 :
            mem1 = memberConnect[mem1]
        if memberConnect[mem2] != mem2 :
            mem2 = memberConnect[mem2]
        if memberConnect[mem1] == mem1 and memberConnect[mem2] == mem2 :
            break
    money[mem1] += money[mem2]
    money[mem2] = 0
    memberConnect[mem2] = mem1

    #print(memberConnect)

for i in money :

#print(money)
#print(memberConnect)

if result :
    print("POSSIBLE")
else :
    print("IMPOSSIBLE")