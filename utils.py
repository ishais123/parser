import json
import pandas as pd
import matplotlib.pyplot as plt
import argparse


def test():
  print("test")


def parse_args():
    parser = argparse.ArgumentParser(description='Parser tool for AWS logs')
    parser.add_argument("-f", "--file", help="Log file location")
    args = parser.parse_args()
    return args


def parse_logs(file):
  parsed_logs = []
  with open(file, 'r') as file:
    for line in file.readlines():
      d = dict()
      if len(line.split(' - ')) >= 4:
        d['Date'] = line.split(' - ')[0]
        d['log_Type'] = line.split(' - ')[1]
        d['event'] = line.split(' - ')[2]
        d['event_attr'] = line.split(' - ')[3]
        parsed_logs.append(d)
      elif len(line.split(' - ')) >= 3:
        d['Date'] = line.split(' - ')[0]
        d['log_Type'] = line.split(' - ')[1]
        d['event'] = line.split(' - ')[2]
        parsed_logs.append(d)
    return parsed_logs


def parse_datetime(datetime):
  if len(datetime.split(' ')) >= 2:
    date = datetime.split(' ')[0]
    time = datetime.split(' ')[1]
  return date, time


def parse_event(event):
  event_types = ["create", "delete", "add", "remove", "modify", "hard-modify"]
  for event_type in event_types:
    if event_type in event:
      if len(event.split(' ')) == 2:
        event_type = event.split(' ')[0]
        event_resource = event.split(' ')[1]
        return event_type, event_resource
      else:
        return False


def parse_prev_log(log):
  event = log.get('event')
  splited_log = event.split(' ')
  for index, word in enumerate(splited_log):
    if word == "performed":
      return splited_log[index+1]


def check_scan(log):
  event = log.get('event')
  if "Scanning" in event:
    return True
  else:
    return False


def graph_generator(data):
  data = json.dumps({
    "success": True,
    "data": data
  })

  data = json.loads(data)
  dates = [i['time'] for i in data["data"]]
  values = [i['event_type'] for i in data['data']]

  df = pd.DataFrame({'dates': dates, 'values': values})
  df['dates'] = [pd.to_datetime(i) for i in df['dates']]

  print(df.sort_values(by='dates'))

  plt.bar(dates, values)
  plt.show()
  return 0
