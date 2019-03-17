import time
import json, socket
from enum import Enum
import ev3dev.ev3 as ev3

## helper functions ##

def _send(socket, data):
  try:
    serialized = json.dumps(data)
  except (TypeError, ValueError):
    raise Exception('You can only send JSON-serializable data')
  # send the length of the serialized data first
  socket.send(bytes('%d\n' % len(serialized), 'utf8'))
  # send the serialized data
  socket.sendall(bytes(serialized, 'utf8'))

def _recv(socket):
  # read the length of the data, letter by letter until we reach EOL
  length_str = ''
  char = socket.recv(1).decode("ascii")
  while char != '}':
    length_str += char
    char = socket.recv(1).decode("ascii")
  string = length_str.split("\n")[1]+"}"
  return json.loads(string)

  # total = int(length_str)
  # # use a memoryview to receive the data chunk by chunk efficiently
  # view = memoryview(bytearray(total))
  # next_offset = 0
  # while total - next_offset > 0:
  #   recv_size = socket.recv_into(view[next_offset:], total - next_offset)
  #   next_offset += recv_size
  # try:
  #   deserialized = json.loads(view.tobytes())
  # except (TypeError, ValueError):
  #   raise Exception('Data received was not in JSON format')
  # return deserialized


class Client(object):
  """
  A JSON socket client used to communicate with a JSON socket server. All the
  data is serialized in JSON. How to use it:

  data = {
    'name': 'Patrick Jane',
    'age': 45,
    'children': ['Susie', 'Mike', 'Philip']
  }
  client = Client()
  client.connect(host, port)
  client.send(data)
  response = client.recv()
  # or in one line:
  response = Client().connect(host, port).send(data).recv()
  """

  socket = None

  def __del__(self):
    self.close()

  def connect(self, host, port):
    self.socket = socket.socket()
    self.socket.connect((host, port))
    return self

  def send(self, data):
    if not self.socket:
      raise Exception('You have to connect first before sending data')
    _send(self.socket, data)
    return self

  def recv(self):
    if not self.socket:
      raise Exception('You have to connect first before receiving data')
    return _recv(self.socket)

  def recv_and_close(self):
    data = self.recv()
    self.close()
    return data

  def close(self):
    if self.socket:
      self.socket.close()
      self.socket = None


def move_left(m, m1, value=1000):
    m.run_timed(speed_sp=value, time_sp=400)
    m1.run_timed(speed_sp=value,time_sp=400)

def move_right(m2, m3, value=1000):
    m2.run_timed(speed_sp=value, time_sp=400)
    m3.run_timed(speed_sp=value,time_sp=400)

def go_forward(m, m1, m2, m3, value=1000):
    move_left(m ,m1, value)
    move_right(m2, m3, value)

class Type(Enum):
    FORWARD="forward"
    STOP="stop"

if __name__ == "__main__":
    # host = 'LOCALHOST'
    host = '192.168.105.135'
    port = 5004

    m=ev3.LargeMotor('outA')
    m1=ev3.LargeMotor('outB')
    m2=ev3.LargeMotor('outC')
    m3=ev3.LargeMotor('outD')
    if not (m.connected):
        print("Plug a motor into port A")
    elif not (m1.connected):
        print("Plug a motor into port B")
    elif not (m2.connected):
        print("Plug a motor into port C")
    elif not (m3.connected):
        print("Plug a motor into port D")
    else:
        while True:
            client = Client()
            client.connect(host, port)
            response = client.recv()
            if(response['type']==Type.FORWARD.value):
                go_forward(m, m1, m2, m3)
                print(response, "FORWARD")
            if(response['type']==Type.STOP.value):
                print(response, "STOP")
            time.sleep(2)
            client.close()
