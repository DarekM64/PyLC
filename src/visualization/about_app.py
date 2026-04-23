import customtkinter as ctk
from tkinter import Label, Toplevel
import tkinter.font as tkFont
def show_about(parent):

    top = Toplevel(parent,width = 400, height = 300)
    
    _Roboto36 = tkFont.Font(family="Roboto",size=36,weight="bold")
    _OpenSans20 = tkFont.Font(family="Open Sans",size=20,weight="bold")
    description='''
    Program simulating simple ladder program for PLC.
    
    Tool to get familiar with ladder programming, no PLC needed.

    
    '''

    by_txt= 'By Dariusz M'

    top.title("PyLC")
    #top.geometry("600x400")
    label = Label(top, text='PyLC', font=_Roboto36)
    label.pack(anchor='n',side='top')
    description_label = Label(top, text=description, font=_OpenSans20)
    description_label.pack(side='left')
    by_label = Label(top, text=by_txt, font=_OpenSans20)
    by_label.pack(anchor='se', side='bottom')


    top.geometry("")