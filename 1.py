print ('введите дату:')
try:
    n=float(input())
except ValueError:
    print('ошибка ввода данных')
else:
    m=(n*100)%100
    d=(n*100)//100
    if m==1 and 1<=d<=31:
       print("январь")
    elif m==2 and 1<=d<=29:
        print("февраль")
    elif m==3 and 1<=d<=31:
        print("март")
    elif m==4 and 1<=d<=30:
        print("апрель")
    elif m==5 and 1<=d<=31:
        print("май")
    elif m==6 and 1<=d<=30:
        print("июнь")
    elif m==7 and 1<=d<=31:
        print("июль")
    elif m==8 and 1<=d<=31:
        print("август")
    elif m==9 and 1<=d<=30:
        print("сентябрь")
    elif m==10 and 1<=d<=31:
        print("октябрь")
    elif m==11 and 1<=d<=30:
        print("ноябрь")
    elif m==12 and 1<=d<=31:
        print("декабрь")        
    else: print("ошибка ввода данных")
