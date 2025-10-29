def grade(score):
    if score>=90:
        return "A" 
    elif score>=80 and score<90:
        return "B" 
    elif score>=70 and score<80:
        return "C" 
    else:
        return "F"
marks=int(input())
print(grade(marks))