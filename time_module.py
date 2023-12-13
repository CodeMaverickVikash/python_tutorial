# Module to work with date and time
# import time

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)

# k=0
# while(k<3):
#     print("this is vikash")
#     time.sleep(2)
#     k+=1


# import datetime

# x = datetime.datetime.now()

# print(x._year)
# print(x.strftime("%A"))

# from datetime import date, time, datetime # date class
import time

# seconds passed since epoch
seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)

