n = int(input())
s = input()

d_score = s.count("D")
a_score = s.count("A")

if d_score>a_score:
    print("Danik")
elif a_score>d_score:
    print("Anton")
else:
    print("Friendship")
