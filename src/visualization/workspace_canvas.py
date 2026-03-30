from customtkinter import CTkFrame, CTkScrollbar
from tkinter import Canvas

def init_workspace(master,bg_color='green', fg_color='green'):

    canvas_frame = CTkFrame(master=master,
                                bg_color=bg_color,
                                fg_color=fg_color,)


    
    canvas_frame.pack(side='bottom',fill='both', expand=True)

    canvas_frame.grid_rowconfigure(0, weight=1) 
    canvas_frame.grid_columnconfigure(0, weight=1)

    # create scrollable textbox
    canvas = Canvas(master=canvas_frame,scrollregion=(0,0,1000,3000))
    canvas.grid(row=0, column=0, sticky="nsew",padx=0,pady=0)
    # create CTk scrollbar
    ctk_canvas_scrollbar = CTkScrollbar(canvas_frame, command=canvas.yview, )
    ctk_canvas_scrollbar.grid(row=0, column=1, sticky="ns")

    # connect textbox scroll event to CTk scrollbar
    canvas.configure(yscrollcommand=ctk_canvas_scrollbar.set)

    return canvas