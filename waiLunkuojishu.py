# --* coding: utf-8 *--
import cv2
import numpy as np 
import tkinter as tk
import tkinter.font as tkFont
import imutils


def login_1():
    print("login")
    pass


def add_1():
    if lbzsl.get() == '':
        v1.set('0')
    if lbdql.get() == '':
        v2.set('0')
    # result = int(lbdql.get())
    result = int(lbzsl.get()) + int(lbdql.get())
    v1.set(result)
    v2.set('0')
    # lbdql.delete(0,tk.END)
    print('add')
    pass


def clear_():
    v1.set('0')
    v2.set('0')

def count_1():
    global ret
    #cap = cv2.VideoCapture('http://192.168.0.105:8080/shot.jpg')
    cap = cv2.VideoCapture(1)
    ret,image = cap.read()

    # image = cv2.imread(r'C:\Users\00597\Pictures\images\zhouChen.jpg')
    image = cv2.resize(image,(800,600),interpolation = cv2.INTER_CUBIC)

    img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # equ = cv2.equalizeHist(img) #均衡二值图

    blurred = cv2.GaussianBlur(img,(5,5),0)
    ret,thresh = cv2.threshold(blurred,40,255,cv2.THRESH_BINARY_INV)
    #ret,thresh = cv2.threshold(blurred,100,255,cv2.THRESH_BINARY_INV)
    # blurred = cv2.GaussianBlur(gray,(5,5),0)
    # ret,thresh = cv2.threshold(blurred,180,255,cv2.THRESH_BINARY)
    # ret,thresh = cv2.threshold(blurred,40,255,cv2.THRESH_BINARY_INV)
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(thresh,kernel,iterations = 1)
    cv2.namedWindow('thresh')
    cv2.imshow('thresh',erosion)
    cv2.namedWindow('image')
    cv2.imshow('image',img)

    cnts = cv2.findContours(erosion.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cap.release()


    # count = (len(cnst))[]
    v2.set(len(cnts))

    print(len(cnts))
    #pass


root = tk.Tk()


v1 = tk.StringVar()
v2 = tk.StringVar()
v3 = tk.StringVar()

ft = tkFont.Font(family = 'Fixdsys',size = 28,weight = tkFont.BOLD)

root.title('轴承计数')
root.geometry('600x440')

#cvs = tk.Canvas(root,bg = 'white')
#cvs.pack(padx =10,pady = 10)
countFm = tk.LabelFrame(root)
countFm.pack(padx = 10 ,pady =10)

lbzs = tk.Label(countFm,text = '总数:',font = ft,anchor = tk.NW)
lbzs.grid(row = 0,column= 0)

lbdq = tk.Label(countFm,text = '当前数量:',font = ft,anchor = tk.NW)  
lbdq.grid(row = 1 ,column= 0)

lbzsl = tk.Entry(countFm,textvariable = v1,font = ft)
lbzsl.grid(row = 0,column= 1)

lbdql = tk.Entry(countFm,textvariable = v2,font = ft)
#lbdql = tk.Label(countFm,text = '0',font = ft)
lbdql.grid(row = 1,column= 1)

lbfm = tk.LabelFrame(root)
lbfm.pack(padx =10,pady = 10)

login1 = tk.Button(lbfm,text = '登陆',font = ft,command = login_1)
#login1.pack(padx = 5,pady = 5)
login1.grid(row = 0,column= 0,padx =5,pady=5)

add1 = tk.Button(lbfm,text = '+',font = ft,command = add_1)
add1.grid(row = 0,column= 1,padx =5,pady=5)

count1 = tk.Button(lbfm,text = '计数',font = ft,command = count_1)
# count1 = tk.Button(lbfm,text = '计数',font = ft,command = lambda:count_1(count1,lbdql))
count1.grid(row = 0,column= 2,padx =5,pady=5)

quit1 = tk.Button(lbfm,text = '退出',font = ft,command = root.quit)
quit1.grid(row = 1,column= 1,padx =5,pady=5)

cl = tk.Button(lbfm,text = '清零',font = ft,command = clear_)
cl.grid(row = 1,column= 0,padx =5,pady=5)

root.mainloop()



