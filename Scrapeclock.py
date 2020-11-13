from datetime import date

from apscheduler.schedulers.blocking import BlockingScheduler

from SimpleScrape import *

sched = BlockingScheduler()

# Schedule job_function to be called every 24hrs from a certain date at 7:30am Canberra time
sched.add_job(send_goodtimes, 'interval', hours=24, start_date='2010-10-01 20:30:00')
sched.start()
