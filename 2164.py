# BOJ _ 2164 카드2

n = int(input())
from collections import deque
cards = deque([i for i in range(1,n+1)])

while True:
    if len(cards) <= 1:
        print(*cards)
        break
    else: 
        cards.popleft()
        cards.append(cards.popleft())



# 재귀 코드 (메모리초과)

n = int(input())
from collections import deque
cardlst = deque([i for i in range(1,n+1)])
def card(n):
    if len(cardlst) <= 1:
        return cardlst
    else:
        cardlst.popleft()
        cardlst.append(cardlst.popleft())
        return card(n)

print(*card(n))