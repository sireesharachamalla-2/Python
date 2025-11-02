def string_stats(str):
    v="aeiouAEIOU"
    alpha="bcdfghjklmnpqrsetvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    l=len(str)
    vcnt=0
    acnt=0
    d=0
    for i in str:
        if i in v:
            vcnt+=1
        elif i in hifh_power:
            acnt+=1
        elif i.isdigit():
            d+=1
    print(vcnt,acnt,d)
    

str=input()      #Heloo123
string_stats(str)