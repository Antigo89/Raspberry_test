import os
import glob
import time
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QLCDNumber
import therm_monitor

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:]!='YES':
        time.sleep(0.2)
        lines = read_lines_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string)/1000.0
        temp_f = temp_c*9.0/5.0+32.0
        return temp_c, temp_f
    

    
class ExampleApp(QtWidgets.QMainWindow, therm_monitor.Ui_MainWindow, QLCDNumber):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTherm)
        self.timer.start(1000)
        
    def showTherm(self):
        lines = read_temp_raw()
        while lines[0].strip()[-3:]!='YES':
            time.sleep(0.2)
            lines = read_lines_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = round(float(temp_string)/1000.0, 2)
            temp_f = round(temp_c*9.0/5.0+32.0, 2)
            self.therm_c.display(str(temp_c))
            self.therm_f.display(str(temp_f))
        
def main():
    app = QtWidgets.QApplication(sys.argv) 
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()  
  

    
