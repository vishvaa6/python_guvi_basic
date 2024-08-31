from datetime import datetime

# Getting the current date and time
dt = datetime.now()
file = "timestamp.txt"


def date_time(file_name,content):
    file = open(file_name,'w')
    file.write(str(content))
    file.close()

date_time(file,dt)    