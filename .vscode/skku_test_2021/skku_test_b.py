'''
예술가 민정이는 바람에 자유롭게 회전해도 알아볼 수 있는 표지판을 만들려고 한다. 
이러한 표지판을 만들기 위해 민정이는 180도 회전해도 변하지 않는 문자인 H, I, N, O, S, X, Z 만을 사용할 수 있다.

단어를 보고, 그 단어가 회전 표지판­에 사용될 수 있는지를 결정하는 프로그램을 작성하라.
'''

CharList = ['H', 'I', 'N', 'O', 'S', 'X', 'Z']
word = input()
result = 'YES'

for i in word :
    if i not in CharList :
        result = 'NO'
        break

print(result)