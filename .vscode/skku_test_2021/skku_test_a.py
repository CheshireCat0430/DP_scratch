'''
처음으로 인사캠을 방문한 율전이는 너무나 가파른 오르막길에 놀랐다. 
이를 본 율전이는 인사캠의 경사가 얼마나 심한지 알기 위해 네 지점의 높이를 측정하기로 마음먹었다. 
이때 율전이는 측정한 높이를 다음과 같이 네 가지 경우로 나누려고 한다. (단, 측정한 순서는 유지한다)

1. 4개의 증가(strictly increasing)하는 높이를 읽은 경우(“Uphill”) (예: 3 4 7 9)
2. 4개의 감소(strictly decreasing)하는 높이를 읽은 경우(“Downhill”) (예: 9 6 5 2)
3. 4개의 일정한 높이를 읽은 경우(“Flat Land”) (예: 5 5 5 5)
4. 위 경우 중 어느 것에도 속하지 않는 경우(“Unknown”)

율전이가 측정한 높이가 주어졌을 때, 어떤 경우에 속하는지 출력하라.
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a<b & b<c & c<d :
    print("Uphill")
elif a>b & b>c & c>d :
    print("Downhill")
elif a==b & b==c & c==d :
    print("Flat Land")
else :
    print("Unknown")
