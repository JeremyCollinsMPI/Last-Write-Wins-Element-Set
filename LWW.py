import time

class LWW():
  def __init__(self, bias='add', time_precision = 7):
    self.add_set = {}
    self.remove_set = {}
    self.set = []
    self.bias = bias
    self.time_precision = time_precision

  def add(self, element):
    current_timestamp = round(time.time(), self.time_precision)
    self.add_set[element] = current_timestamp

  def remove(self, element):
    current_timestamp = round(time.time(), self.time_precision)
    self.remove_set[element] = current_timestamp

  def exists(self, element):
    try:
      last_add_timestamp = self.add_set[element]
    except:
      return False
    try:
      last_remove_timestamp = self.remove_set[element]
    except:
      return True
    if last_add_timestamp > last_remove_timestamp:
      return True
    elif last_add_timestamp == last_remove_timestamp and self.bias == 'add':
      return True
    else:
      return False

  def merge_with(self, LWW2):
    for member in LWW2.add_set.keys():
      try:
        timestamp1 = self.add_set[member]
      except:
        self.add_set[member] = LWW2.add_set[member]
        continue
      timestamp2 = LWW2.add_set[member]
      self.add_set[member] = max(timestamp1, timestamp2)
    for member in LWW2.remove_set.keys():
      try:
        timestamp1 = self.remove_set[member]
      except:
        self.remove_set[member] = LWW2.remove_set[member]
        continue
      timestamp2 =  LWW2.remove_set[member]
      self.remove_set[member] = max(timestamp1, timestamp2)

  def update(self):
    self.set = []
    for member in self.add_set.keys():
      try:
        last_remove_timestamp = self.remove_set[member]
      except:
        self.set.append(member)
        continue
      last_add_timestamp = self.add_set[member]
      if last_add_timestamp > last_remove_timestamp:
        self.set.append(member)
      if last_add_timestamp == last_remove_timestamp and self.bias == 'add':
        self.set.append(member)
