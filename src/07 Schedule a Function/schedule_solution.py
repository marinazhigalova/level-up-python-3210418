import sched
import time

def schedule_function(target_time, func, *args):
  scheduler = sched.scheduler(time.time, time.sleep)
  scheduler.enterabs(target_time, 1, func, args)
  scheduler.run()

# commands used in solution video for reference
if __name__ == '__main__':
    schedule_function(time.time() + 1, print, 'Howdy!')
    schedule_function(time.time() + 1, print, 'Howdy!', 'How are you?')
    schedule_function(time.time() + 1, print, 'Howdy!', 'How are you?', 'Alive?????')