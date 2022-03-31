player=["황의조", "황희찬", "구자철", "이재성", "기성용"]
print("현재 경기 중인 선수:")
for p in player:
    print(p)
print("-----------------------------------------------")
n = input("OUT 시킬 선수 번호: ")
n=int(n)
na = input("IN 할 선수 이름: ")
print("-----------------------------------------------")
del player[n]
player.append(na)
print("교체 결과:")
print(player)