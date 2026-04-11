import threading
import time

from src.ladder.ladder_elements import *
from src.ladder.ladder_solver import *

#TODO Add clock feature for simulation
#TODO Add binding plc data and ladder elements

class PLC:

    def __init__(self,M=100):
        self.rungs=[]
        self.M=[[False] for i in range(M)]
        self.main_thread = threading.Thread(target=self.plc_main_program)
        self.run=False
        self.close_thread = False

    
    def plc_main_program(self):
        while True:
            while self.run:
                print('Start evaluating rungs')
                for rung in self.rungs:
                    evaluate_rung(rung)
                    time.sleep(1)
                print('All rungs solved')
            if self.close_thread:
                break
        print('Closing plc main program thread')

    def start(self):
        self.run = True
        self.main_thread.start()

    def stop(self):
        self.run = False

    def get_data(type, address):
        match type:
            case 'M':
                return self.M[address] 

    def bind_data(self,type='M', address = 0):
        match type:
            case 'M':
                return self.M[address]
        

def evaluate_rung(rung:Rung):
        solve_rung(rung)
