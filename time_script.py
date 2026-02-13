import requests
import datetime
import win32api
import sys

def win_set_time(time_tuple):
    
    # http://timgolden.me.uk/pywin32-docs/win32api__SetSystemTime_meth.html
    # pywin32.SetSystemTime(year, month , dayOfWeek , day , hour , minute , second , millseconds )
    dayOfWeek = datetime.datetime(*time_tuple).isocalendar()[2]
    system_time = time_tuple[:2] + (dayOfWeek,) + time_tuple[2:]
    print(system_time)
    win32api.SetSystemTime(*system_time)

try:

    response = requests.get("https://timeapi.io/api/v1/time/current/zone?timezone=Asia/Kolkata")
    api_time = response.json()
    hour = (int(api_time['time'][:2])-5)
    mint = (int(api_time['time'][3:5])-30)
    if mint<0:
        mint = 60+mint
        hour = hour-1
    if hour<0:
        hour = 24+hour

    time_tuple = ( int(api_time['date'][:4]), # Year
                int(api_time['date'][5:7]), # Month
                int(api_time['date'][8:10]), # Day
                hour, # Hour
                mint, # Minute
                int(api_time['time'][6:8]), # Second
                    0, # Millisecond
                )
    print(time_tuple)
    win_set_time(time_tuple)
except:
    sys.exit()