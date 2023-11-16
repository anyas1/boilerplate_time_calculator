def add_time(start, duration, day = None):
  new_day = None
  plus_days = 0

  days = [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
  ]
  starting_hour = int(start.split(':')[0])
  starting_minute = int((start.split(':')[1]).split()[0])
  day_time = start.split()[1]

  added_hour = int(duration.split(':')[0])
  added_minute = int(duration.split(':')[1])

  if day_time == 'PM':
    starting_hour = starting_hour + 12

  new_hour = starting_hour + added_hour
  new_minute = starting_minute + added_minute

  if new_minute >= 60:
    new_minute = new_minute - 60
    new_hour = new_hour + 1

  if new_minute < 10:
    new_minute = f'0{new_minute}'

  if new_hour >= 24 and new_hour < 48:
    plus_days = new_hour // 24
    new_day = '(next day)'

  if new_hour >= 48:
    plus_days = new_hour // 24
    new_day = f"({plus_days} days later)"

  if new_hour >= 24:
    new_hour = new_hour % 24

  if new_hour < 12:
    day_time = 'AM'
  else:
    day_time = 'PM'

  if new_hour >= 12:
    new_hour = new_hour - 12
  
  if new_hour == 0:
    new_hour = 12

  if day != None:
    week_day = day.lower().capitalize()
    day_index = days.index(week_day)
    week_day = days[(day_index + plus_days) % len(days)]
  
  if new_day == None:
    new_time = f"{new_hour}:{new_minute} {day_time}"

  if day != None:
    new_time = f"{new_hour}:{new_minute} {day_time}, {week_day}"

  if new_day != None and day == None:
    new_time = f"{new_hour}:{new_minute} {day_time} {new_day}"

  if new_day != None and day != None:
    new_time = f"{new_hour}:{new_minute} {day_time}, {week_day} {new_day}"

  return new_time
