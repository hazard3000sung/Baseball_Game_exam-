import random
import tkinter as tk
import tkinter.messagebox as tmsg


def ButtonClick():
    b = editbox1.get()
    tmsg.showinfo("Number", b)
    isok = False
    if len(b) != 4:
        tmsg.showerror("error", "Write in 4 number")
    else:
        numberok = True
        for i in range(4):
            if (b[i] < "0") or (b[i] > "9"):
                tmsg.showerror("error", "It's not a integer")
                numberok = False
                break
            if numberok:
                isok = True
    if isok:
        hit = 0
        for i in range(4):
            if a[i] == int(b[i]):
                hit = hit + 1
        blow = 0
        for j in range(4):
            for i in range(4):
                if (int(b[j]) == a[j]) and (a[i] != int(b[j])) and (a[j] != int(b[j])):
                    blow = blow + 1
                    break
        if hit == 4:
            tmsg.showinfo("collect!!!.", "congratuations.")
            root.destroy()
            tmsg.showinfo("hit", "hit" + str(hit) + "/" + "ball" + str(blow))
        else:
            historybox.insert(tk.END, b + "/H:" + str(hit) + "B:" + str(blow) + "\n")


a = [random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9)]

root = tk.Tk()
root.geometry("600x400")
root.title("Hit your number!")
historybox = tk.Text(root, font=("as you want", as you want))
historybox.place(x=400, y=0, width=200, height=400)

label1 = tk.Label(root, text="Input Number", font=("Helvetica", 14))
label1.place(x=5, y=5)
label2 = tk.Label(root, text="OOUCH", font=("Helvetica", 10))
label2.place(x=30, y=30)
editbox1 = tk.Entry(width=4, font=("Helvetica", 10))
editbox1.place(x=180, y=8)
button1 = tk.Button(root, text="check", font=("Helvetica", 14),
                    command=ButtonClick)
button1.place(x=220, y=60)

root.mainloop()
