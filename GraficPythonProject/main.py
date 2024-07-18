import datetime
from GraficPythonProject.bd import BDGraf
bd=BDGraf()
current_date = datetime.datetime.now().strftime('%d.%m.%Y')
date=""


##print(current_date)



##print(bd.select_change_date(current_date))


##print(bd.sqlite_master())
##print(bd.select_user())

##import sqlite3

#Формат даты ('%d.%m.%Y')
def working_today(date):
    if(date==""):
        date = current_date
        return  decoding_record(bd.select_change_date(date))
    else:
        return decoding_record(bd.select_change_date(date))

def decoding_record(table):

    for line_change_date in table:
       print(bd.select_users(str(line_change_date[2]))+bd.select_change(str(line_change_date[3])))


def cost_of_shift():



#a = "01.06.2024"
#print(working_today(a))