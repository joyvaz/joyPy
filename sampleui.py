print('This is my first UI Project')
from tkinter import *
import tkinter.font as tkFont
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter import messagebox

top = Tk()
top.geometry("500x300")
Title = top.title( "PDF Reader Utility v0.1")
fontStyle = tkFont.Font(family="Lucida Grande", size=14)
heading = Label(top,text="WEL-COME TO PDF READER", anchor = "center", font=fontStyle)

def getUploadedFileName(filePath):
    splitArr = filePath.split('/')
    if(splitArr[-1].endswith('.pdf')):
        return splitArr[-1]
    else:
        return 'Invalid File. Please upload file having .pdf extension'

def OpenFile():
    selectFile = askopenfile(title='Please select pdf file...',
                        filetypes=[('pdf File', ['.pdf'])])
    try:
        global filename
        filename = selectFile.name
        global lblFilePath
        lblFilePath = Label(top, text = getUploadedFileName(selectFile.name), font = ("Lucida Grande", 8))
        lblFilePath.place(x=225, y = 50)
        btnProcess["state"] = "normal"
    except Exception as e:
        print("Failed to select file: ", e)

    
def ProcessFile(fileToBeProcessed):
    btnProcess["state"] = "disabled"
    btnProcess["text"] = "Processing..."
    # msg=messagebox.showinfo( "File Processing", fileToBeProcessed)
    if(startProcessing(fileToBeProcessed)):
        global lblprocessPath
        lblprocessPath = Label(top, text = 'File processed successfully', font = ("Lucida Grande", 8))
        lblprocessPath.place(x=150, y = 150)

def startProcessing(filepathToProcess):
    print('I am processing:', filepathToProcess)
    return True

def ResetForm():
    lblFilePath.destroy()
    lblprocessPath.destroy()
    filename = ''
    btnProcess["state"] = "disabled"
    btnProcess["text"] = "Process"
    print(filename)
    msg=messagebox.showinfo("Form Reset", 'Form reset successfully!')

lblBrowser = Label(top, text = 'Selet PDF file to read: ', font = ("Lucida Grande", 10))
btnBrowser = Button(top, text='Browse', height = 1,width = 7, command = OpenFile )
btnProcess = Button(top, text ="Process", height = 1, state = 'disabled', command = lambda: ProcessFile(filename))    
btnClear = Button(top, text ="Reset", height = 1, width = 7, command = ResetForm)    

heading.place(x=130,y=10)
lblBrowser.place(x=10, y = 50)
btnBrowser.place(x=150, y = 50)
btnProcess.place(x=50, y = 100)
btnClear.place(x=150, y = 100)
top.mainloop()
