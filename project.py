import os, re

def run():
  file = open('data-sample.log', 'r')
  lines = file.readlines()

  count = 0
  #regex = re.search("Priority: [3-9]". line)

  for line in lines:
    count += 1
    regex = str(re.search("Priority: [3-9]", line))
    if (regex == "None"):
      pass
    else:
      print('line: ' + str(count) + ' - ' + line)

if __name__ == '__main__':
  run()
