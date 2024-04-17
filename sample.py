import os
 
print('Absolute path of file:     ', 
      os.path.abspath('instance-status.csv'))
print('Absolute directoryname: ', 
      os.path.dirname(os.path.abspath(__file__)))

print("Hello World")