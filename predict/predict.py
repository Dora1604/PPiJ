from datetime import date
def pretvori(mjesec):
    if mjesec==1:
        return "JANUARY"
    elif mjesec==2:
        return "FEBRUARY"
    elif mjesec==3:
        return "MARCH"
    elif mjesec==4:
        return "APRIL"
    elif mjesec==5:
        return "MAY"
    elif mjesec==6:
        return "JUNE"
    elif mjesec==7:
        return "JULY"
    elif mjesec==8:
        return "AUGUST"
    elif mjesec==9:
        return "SEPTEMBER"
    elif mjesec==10:
        return "OCTOBER"
    elif mjesec==11:
        return "NOVEMBER"
    else:
        return "DECEMBER"
rjecnik={"JANUARY":{},"2":{},"JUNE":{}}
l = ["1","2"]
for i in l:
    datum = date.today()
    key = pretvori(datum.month)
    rjecnik[key][str(datum)] = 5
print(rjecnik)