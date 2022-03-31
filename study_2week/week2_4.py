string1="브이넥 라이트 다운 베스트"
string2="    25,990원    "

string2=string2.strip()
print(string2)

string2=string2.replace(",","")
string2=string2[:-1]
print(string2)

print(int(string2)+100)