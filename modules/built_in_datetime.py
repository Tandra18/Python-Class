# import datetime
#
# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.strftime("%A"))
#
#
# y = datetime.datetime(2019,1,15)
# print(y)



from datetime import datetime
import pytz

yangon_tz = pytz.timezone('Asia/Yangon')
z = yangon_tz.localize(datetime(2019,1,15,14,30))
print(z)
# print(z.strftime('%B'))
#
# x = pytz.all_timezones
# print(x)

