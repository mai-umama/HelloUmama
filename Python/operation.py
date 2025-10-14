S = input()
T = input()
rep = 0

for s_idx, t_idx in zip(S,T):
    if(s_idx != t_idx):
        rep+=1
print(rep)
