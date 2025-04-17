import utils

args = utils.parse_args()

if True:
 print("this is true")

if args.file:
  LOG_FILE_LOCATION = args.file
  print(LOG_FILE_LOCATION)
else:
  LOG_FILE_LOCATION = 'trail.log'
  print("No log file provided, using default trail.log")

def main():
  output = []
  output_log = dict()

  try:
    res_parse_logs = utils.parse_logs(LOG_FILE_LOCATION)

  except FileNotFoundError as e:
    print(e)
    exit(1)

  for index, log in enumerate(res_parse_logs):
    event = log.get('event')
    res_parse_event = utils.parse_event(event)
    if res_parse_event:
      prev_log = res_parse_logs[index - 1]
      next_log = res_parse_logs[index + 1]

      datetime = utils.parse_datetime(log.get('Date'))
      output_log['date'] = datetime[0]
      output_log['time'] = datetime[1]

      output_log['event_type'] = res_parse_event[0]
      output_log['event_resource'] = res_parse_event[1]

      action = utils.parse_prev_log(prev_log)
      output_log['action'] = action

      if utils.check_scan(next_log):
        output_log['scan'] = "True"
      else:
        output_log['scan'] = "False"

      output_log['event_attr'] = log['event_attr']
      output.append(output_log)
      output_log = {}

  utils.graph_generator(output)


if __name__ == '__main__':
    main()
