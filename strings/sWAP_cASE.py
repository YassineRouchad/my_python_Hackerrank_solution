""" create a function that do the following Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  """
import string
Upp=list(string.ascii_uppercase)
Low=list(string.ascii_lowercase)
def swap_case(s):
    S=list(s)
    for i in range(len(S)):
        for j in range(len(Upp)):
            if(S[i]==Upp[j]):
                S[i]=Low[j]
            elif(S[i]==Low[j]):
                S[i]=Upp[j]
    S="".join(S)
    return S    
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
