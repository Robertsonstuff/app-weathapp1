from datetime import date

from apscheduler.schedulers.blocking import BlockingScheduler

from SimpleScrape import *

sched = BlockingScheduler()

# Schedule job_function to be called every blah
#sched.add_job(send_goodtimes, 'interval', seconds=30)
sched.add_job(send_goodtimes, 'interval', hours=24, start_date='2010-10-01 20:30:00')
sched.start()