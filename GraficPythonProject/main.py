import datetime
from GraficPythonProject.bd import BDGraf
import json
import requests
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
        return  decoding_record(bd.select_chart_date(date))
    else:
        return decoding_record(bd.select_chart_date(date))

def decoding_record(table):
    message = ""
    for line_change_date in table:

        name_user = bd.select_user(str(line_change_date[2]))
        change_date = bd.select_change_id(str(line_change_date[3]))
        #print(line_change_date)
        for user in name_user:
            message += user[2]
        for date in change_date:
            message += ": "+date[2]+ " - "+date[3] + "\n"

    return message




#bd.insert_chart(current_date,2,	5)

def check_weekends(date):
    date_usa=date[-4:]+"-"+date[3]+date[4]+"-"+date[:2]
    url = 'https://raw.githubusercontent.com/d10xa/holidays-calendar/master/json/consultant' + date[-4:] + '.json'
    r = requests.get(url)
    cal = json.loads(r.text)
    return cal["holidays"].count(date_usa)
#def shift_analysis(date):

#def select_type_day():

# Ищет где не стоит статус дня и проставляет
def update_type_day():
    type_date = ""
    for date in bd.select_chart_no_type_date():
       #print(date[1])
        #print(check_weekends(date[1]))


       if(check_weekends(date[1])==1):
           print("1")
           bd.update_chart_type_date(date[0],"1")

       else:
           print("Жопа")
           bd.update_chart_type_date(date[0], "0")




#print(bd.select_chart_no_type_date())

    #bd.update_chart_type_date("22","0")

update_type_day()
#bd.connection_commit_and_close()
#def insert_chart_day(change_date,user_id,change_id):

#print(check_weekends("08.07.2024"))
#update_type_day("08.07.2024")

#a = "01.07.2024"
#print(working_today(a))