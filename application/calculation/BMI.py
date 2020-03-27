anser=[]
def BMI(a,b):
    try:
        BMI=b*10000/(a*a)
        anser.append(BMI)

        if BMI<18.5:
            anser.append("あなたは低体重です")
        elif BMI>=18.5 and BMI<25:
            anser.append("あなたは普通体重です")
        else:
            anser.append("あなたは肥満です")
    except:
        anser.append("Error")
        anser.append("Error")
    return anser
