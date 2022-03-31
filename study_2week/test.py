players = ["황의조", "황희찬", "구자철", "이재성", "기성용"]

for p in players:
    print(p)
print("*"*40)
num_out = input("OUT 시킬 선수 번호: ")
name_in = input("IN 할 선수 이름: ")
print("*"*40)
del players[int(num_out)]
players.append(name_in)

print("교체 결과: ")
for p in players:
    print(p)

