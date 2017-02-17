import os
import Tkinter
import tkFileDialog as tkfd

import cylinders as cyl

class main_gui:
    '''
    GUI for Cyltools
    '''
    def __init__(self, root):
        self.root = root

        self.root.title('CylTools')

        self.root.label_text = 'Please select from the following options.'
        self.root.label = Tkinter.Label(self.root, text=self.root.label_text)
        #self.root.label.grid(row=0, columnspan=3)
        self.root.label.pack()

        self.root.cyl_button = Tkinter.Button(self.root, 
                                         text='Cylinders', 
                                         command=self.cyl_gui)
        #self.root.cyl_button.grid(row=1, column=0)
        self.root.cyl_button.pack()

    def cyl_gui(self):
        self.cyl = Tkinter.Toplevel()
        self.cyl_title = 'Cylinder Analysis'
        self.cyl.title(self.cyl_title)
        self.cyl.label = Tkinter.Label(self.cyl, text=self.root.label_text)
        self.cyl.label.pack()

        self.cyl_tracking = Tkinter.Button(self.cyl, 
                                           text='Cylinder Count Tracking',
                                           command=self.cyl_info)
        self.cyl_tracking.pack()

    def cyl_info(self):
        '''
        Retrieves transaction file (CSV), and cylinder type for inquiry
        '''
        self.trans_file = tkfd.askopenfile(initialdir=os.path.expanduser('~')).name

        self.trans = Tkinter.Toplevel()
        self.trans.title('Cylinder Type')

        self.trans.label = Tkinter.Label(self.trans, text='Enter the Cylinder Type')
        self.trans.label.pack()

        self.trans_type = Tkinter.StringVar()
        self.trans.entry = Tkinter.Entry(self.trans, 
                                         textvariable=self.trans_type)
        self.trans.entry.pack()

        self.trans.button = Tkinter.Button(self.trans, text='Enter', 
                                           command=self.cyl_track)
        self.trans.button.pack()

    def cyl_track(self):
        ends = cyl.count_tracking(cyl.read_transactions(self.trans_file),
                                       self.trans_type.get())
        self.text_box(ends)
    

def main():
    main_root = Tkinter.Tk()
    main_app = main_gui(main_root)
    main_root.mainloop()

if __name__ == '__main__':
    main()

