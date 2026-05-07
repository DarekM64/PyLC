# 🧠 PyLC 0.1.2 PLC Ladder Logic Simulator
PLC Ladder Simulator: application simulating PLC functionality in Python. 


A Python-based application for creating and simulating PLC ladder logic (LAD).

This project was developed to combine industrial automation experience with Python programming and to model how real PLC control logic works in a simplified simulation environment.

Code created without AI.

## 🚀 Features
Create ladder logic diagrams (LAD)
Support for Normally Open (NO) contacts
Logical branching (parallel paths)
Multiple coils (outputs) within a single logic segment
Mapping ladder elements to virtual binary variables (PLC-like memory)
Real-time simulation and visualization:
highlighting active logic paths
displaying current states of variables (bits)
Simulation of control logic execution flow

## 🧱 Technologies
Python  
Tkinter  
GitHub  

## 📦 Installation & Setup
#### 1. Clone the repository
  >git clone https://github.com/DarekM64/PyLC.git
  >cd PyLC
#### 2. Create virtual environment
  >python -m venv .venv
#### 3. Activate environment
Windows (PowerShell / VS Code):
  >source .venv/Scripts/activate
Linux / macOS:
  >source .venv/bin/activate
#### 4. Install dependencies
  >pip install -r requirements.txt
#### 5. Install project (editable mode)
  >pip install -e .
#### 6. Run the application
  >python main.py

## 🖥️ How it works

The application allows users to build ladder logic diagrams using:

contacts (NO)
branches (parallel logic paths)
coils (outputs)

Each contact and coil can be linked to a virtual binary variable.

During execution:

active parts of the logic are highlighted
variable states are updated and displayed in real time
logic flow can be visually tracked step-by-step

## 🎯 Project Goals
Improve Python programming skills
Simulate PLC logic behavior in software
Bridge industrial automation experience with modern software development

## 🔧 Future Improvements
Support for additional elements (NC contacts, timers, counters)  
Support for function blocks (ADD, MUL, CMP, MOV etc)  
Save/load projects  
Enhanced UI/UX  
Communication with real PLC devices (e.g. Modbus)  
More PLC devices (R, D, X, Y simulation)  
Web-based version (backend + frontend)  

## 📸 Screenshots

<img width="1316" height="653" alt="image" src="https://github.com/user-attachments/assets/9a26746e-4a9e-4e6b-b2d8-2c8aff8126f8" />







## Implemented Features

-creating ladder program  
-defining PLC M registers for contacts and coils  
-simulating PLC scan  
-write ladder to file  
-read ladder from file


## Roadmap/History

V0.1:   
-simple ladder with contacts creator  
-rung ladder solver


V0.2:  
-simulating plc logic  
-plc memory view  
-write load ladder to file

V0.3:  
--function blocks (ADD, SUB, MOV etc.)  




## 👤 Author
Dariusz Matejkowski
