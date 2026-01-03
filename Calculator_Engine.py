import tkinter as tk
import math

screen = tk.Tk()
screen.title("Simple GUI Example")
screen.geometry("350x500")
screen.configure(bg="gray")


exp = ""

labelframe_e = tk.LabelFrame(screen, padx=15, pady=15, bg="brown", height=20, width=30)
labelframe_e.pack()
entry_cal = tk.Entry(labelframe_e, width=35)
entry_cal.pack()


def plus_s_c():
    global exp
    if '+' in exp:
        number = entry_cal.get().split('+')
        sinexp = number[0]
        cosexp = number[1]
        answer = 0
        if 'sin' in sinexp:
            sinfun(sinexp)
            answer += float(exp)
        if 'cos' in sinexp:
            cosfun(sinexp)
            answer += float(exp)

        if 'cos' in cosexp:
            cosfun(cosexp)
            answer += float(exp)
        if 'sin' in cosexp:
            sinfun(cosexp)
            answer += float(exp)
        if entry_cal.get().isdigit() or 'sin' in sinexp or cosexp or 'cos' in cosexp or sinexp :
            if 'sin' in sinexp:
                sinfun(sinexp)
            if 'sin' in cosexp:
                sinfun(cosexp)
            if 'cos' in cosexp:
                cosfun(cosexp)
            if 'cos' in sinexp:
                cosfun(sinexp)
            num=0
            num+=float(number[0])
            num+=float(number[1])
            answer += float(num)
        exp = str(answer)


def mins_s_c():
    global exp
    if '-' in exp:
        number = entry_cal.get().split('-')
        sinexp = number[0]
        cosexp = number[1]
        answer = 0
        if 'sin' in sinexp :
            sinfun(sinexp)
            answer += float(exp)
        if 'cos' in sinexp:
            cosfun(sinexp)
            answer += float(exp)

        if 'cos' in cosexp:
            cosfun(cosexp)
            answer -= float(exp)
        if 'sin' in cosexp:
            sinfun(cosexp)
            answer -= float(exp)
        else:
            num=sinexp
            num=cosexp
            answer = float(num)
            print('car')
        exp = str(answer)

def mul_s_c():
    global exp
    if '*' in exp:
        number = entry_cal.get().split('*')
        s_p= number[0]
        c_p = number[1]
        answer=0

        if 'sin' in s_p :
            sinfun(s_p)
            answer += float(exp)
        if 'cos' in s_p:
            cosfun(s_p)
            answer += float(exp)

        if 'cos' in c_p:
            cosfun(c_p)
            answer *= float(exp)
        if 'sin' in c_p:
            sinfun(c_p)
            answer *= float(exp)

        exp = str(answer)

def div_s_c():
    global exp
    if '/' in exp:
        number = entry_cal.get().split('/')
        s_pp= number[0]
        c_pp = number[1]
        answer=0

        if 'sin' in s_pp :
            sinfun(s_pp)
            answer += float(exp)
        if 'cos' in s_pp:
            cosfun(s_pp)
            answer += float(exp)

        if 'cos' in c_pp:
            cosfun(c_pp)
            answer /= float(exp)
        if 'sin' in c_pp:
            sinfun(c_pp)
            answer /= float(exp)

        exp = str(answer)









def cosfun(cosexp):
    global exp
    num = cosexp.replace('cos', '').replace('(', '').replace(')', '')
    exp = str(math.cos(math.radians(float(num))))



def sinfun(sinexp):
    global exp
    num = sinexp.replace('sin', '').replace('(', '').replace(')', '')
    exp = str(math.sin(math.radians(float(num))))



def t_b():
    pass


def l_f_1():
    labelframe1 = tk.LabelFrame(screen, bg="brown")
    labelframe1.pack(padx=5, pady=5, )



    def one():
        global exp
        exp += '1'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    one = tk.Button(labelframe1, text="1", command=one, padx=5, pady=5, height=3, width=4, bg="black", fg="white")
    one.pack(side=tk.LEFT, padx=3, pady=3)

    def two():
        global exp
        exp += '2'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    two = tk.Button(labelframe1, text="2", command=two, padx=5, pady=5, height=3, width=4, bg="black", fg="white")
    two.pack(side=tk.LEFT, padx=3, pady=3)

    def three():
        global exp
        exp += '3'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    three = tk.Button(labelframe1, text="3", command=three, padx=5, pady=5, height=3, width=4, bg="black", fg="white")
    three.pack(side=tk.LEFT, padx=3, pady=3)

    def add():
        global exp
        exp = exp + '+'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    add = tk.Button(labelframe1, text="+", command=add, padx=5, pady=5, height=3, width=4, bg="Orange", fg="Black")
    add.pack(side=tk.LEFT, padx=3, pady=3)

    def back_space():
        global exp
        exp = exp[:-1]
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    bs = tk.Button(labelframe1, text='BS', command=back_space, padx=5, pady=5, height=3, width=4, bg="wheat", fg="black")
    bs.pack(side=tk.RIGHT, padx=3, pady=3)



def l_b_2():
    labelframe2 = tk.LabelFrame(screen, bg="brown")
    labelframe2.pack(padx=5, pady=5)



    def four():
        global exp
        exp += '4'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    four = tk.Button(labelframe2, text="4", command=four, padx=5, pady=5, height=3, width=4, bg="black", fg="white")
    four.pack(side=tk.LEFT, padx=3, pady=3)

    def five():
        global exp
        exp += '5'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    five = tk.Button(labelframe2, text="5", command=five, padx=5, pady=5, height=3, width=4, bg="black", fg="white")
    five.pack(side=tk.LEFT, padx=3, pady=3)

    def six():
        global exp
        exp += '6'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    six = tk.Button(labelframe2, text="6", command=six, padx=5, pady=5, height=3, width=4, bg="black", fg="white")
    six.pack(side=tk.LEFT, padx=3, pady=3)

    def mins():
        global exp
        exp = exp + '-'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    sub = tk.Button(labelframe2, text="-", command=mins, padx=5, pady=5, height=3, width=4, bg="Orange", fg="Black")
    sub.pack(side=tk.LEFT, padx=3, pady=3)

    def delete():
        global exp
        exp = ''
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    e = tk.Button(labelframe2, text='De', command=delete, padx=5, pady=5, height=3, width=4, bg="wheat", fg="black")
    e.pack(side=tk.LEFT, padx=3, pady=3)




def l_f_3():
    labelframe3 = tk.LabelFrame(screen, bg="brown")
    labelframe3.pack(padx=5, pady=5)



    def seven():
        global exp
        exp += '7'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    seven = tk.Button(labelframe3, text="7", command=seven, padx=5, pady=5, height=3, width=4, bg="black", fg="white")
    seven.pack(side=tk.LEFT, padx=3, pady=3)

    def eight():
        global exp
        exp += '8'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    eight = tk.Button(labelframe3, text="8", command=eight, padx=5, pady=5, height=3, width=4, bg="black", fg="white")
    eight.pack(side=tk.LEFT, padx=3, pady=3)

    def nine():
        global exp
        exp += '9'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    nine = tk.Button(labelframe3, text="9", command=nine, padx=5, pady=5, height=3, width=4, bg="black", fg="white")
    nine.pack(side=tk.LEFT, padx=3, pady=3)

    def multiply():
        global exp
        exp = exp + '*'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    mul = tk.Button(labelframe3, text="*", command=multiply, padx=5, pady=5, height=3, width=4, bg="Orange", fg="Black")
    mul.pack(side=tk.LEFT, padx=3, pady=3)

    def equal():
        global exp
        if '²' in exp:
            num = exp.replace('²', '')
            exp = str(eval(num + '**2'))
        if '³' in exp:
            num = exp.replace('³', '')
            exp = str(eval(num + '**3'))
        if '√' in exp:
            num = exp.replace('√', '')
            exp = str(eval(num + '**0.5'))



        if 'sin' in exp or 'cos' in exp:

            plus_s_c()
            mins_s_c()
            mul_s_c()
            div_s_c()
            if 'sin' in exp:
                sinfun(exp)
            elif 'cos' in exp:
                cosfun(exp)
            elif 'tan' in exp:
                tanfun()



        if 'sin' in exp:
            sinfun(exp)
        elif 'cos' in exp:
            cosfun(exp)
        elif 'tan' in exp:
            tanfun()

        if 'π' in exp:
            num = exp.replace('π', '')
            exp = str('3.14'+num)
            exp = eval(exp)
            exp = str(exp)
        else:
            exp = eval(exp)
            exp=str(exp)
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)



    def tanfun():
        global exp
        num = exp.replace('tan', '')
        exp = str(math.tan(math.radians(float(num))))

    eq = tk.Button(labelframe3, text="=", command=equal, padx=5, pady=5, height=3, width=4, bg="wheat", fg="black")
    eq.pack(side=tk.RIGHT, padx=3, pady=3)



def l_f_4():
    labelframe4 = tk.LabelFrame(screen, bg="brown")
    labelframe4.pack(padx=5, pady=5)

    def zero():
        global exp
        exp += '0'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    zero = tk.Button(labelframe4, text="0", command=zero, padx=5, pady=5, height=3, width=4, bg="black", fg="white")
    zero.pack(side=tk.LEFT, padx=55, pady=3)



    def divide():
        global exp
        exp = exp + '/'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    div = tk.Button(labelframe4, text="/", command=divide, padx=5, pady=5, height=3, width=4, bg="Orange", fg="Black")
    div.pack(side=tk.LEFT, padx=3, pady=3)

    def pi():
        global exp
        exp += 'π'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    pi = tk.Button(labelframe4, text="π", command=pi, padx=5, pady=5, height=3, width=4, bg="wheat", fg="black")
    pi.pack(side=tk.LEFT, padx=3, pady=3)

def l_f_5():
    labelframe5 = tk.LabelFrame(screen, bg="brown")
    labelframe5.pack(padx=5, pady=5)

    def cube():
        global exp
        exp = exp + '³'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    cube = tk.Button(labelframe5, text='³', command=cube, padx=5, pady=5, height=3, width=4, bg="wheat", fg="black")
    cube.pack(side=tk.LEFT, padx=3, pady=3)

    def cube_r():
        global exp
        exp = exp + '**(1/3)'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    cube_r = tk.Button(labelframe5, text='∛', command=cube_r, padx=5, pady=5, height=3, width=4, bg="wheat", fg="black")
    cube_r.pack(side=tk.LEFT, padx=3, pady=3)

    def bracket1():
        global exp
        exp += '('
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    bracket1 = tk.Button(labelframe5, text='(', command=bracket1, padx=5, pady=5, height=3, width=4, bg="wheat",
                         fg="black")
    bracket1.pack(side=tk.LEFT, padx=3, pady=3)

    def bracket2():
        global exp
        exp += ')'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    bracket2 = tk.Button(labelframe5, text=')', command=bracket2, padx=5, pady=5, height=3, width=4, bg="wheat",
                         fg="black")
    bracket2.pack(side=tk.LEFT, padx=3, pady=3)

    def power():
        global exp
        exp += '**'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)
    power=tk.Button(labelframe5, text='power', command=power, padx=5, pady=5, height=3, width=4, bg="wheat", fg="black")
    power.pack(side=tk.LEFT, padx=3, pady=3)

def l_f_6():
    labelframe6 = tk.LabelFrame(screen, bg="brown")
    labelframe6.pack(padx=5, pady=5)
    def sq():
        global exp
        exp = exp + '²'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    sq = tk.Button(labelframe6, text="²", command=sq, padx=5, pady=5, height=3, width=4, bg="wheat", fg="black")
    sq.pack(side=tk.LEFT, padx=3, pady=3)

    def sqr():
        global exp
        exp = exp + '√'
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    sqr = tk.Button(labelframe6, text="√", command=sqr, padx=5, pady=5, height=3, width=4, bg="wheat", fg="black")
    sqr.pack(side=tk.LEFT, padx=3, pady=3)


    def sins():
        global exp
        exp += 'sin('
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    sin = tk.Button(labelframe6, text='sin', command=sins, padx=5, pady=5, height=3, width=4, bg="wheat", fg="black")
    sin.pack(side=tk.LEFT, padx=3, pady=3)

    def co():
        global exp
        exp += 'cos('
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    cos = tk.Button(labelframe6, text='cos', command=co, padx=5, pady=5, height=3, width=4, bg="wheat", fg="black")
    cos.pack(side=tk.LEFT, padx=3, pady=3)

    def tan():
        global exp
        exp += 'tan('
        entry_cal.delete(0, tk.END)
        entry_cal.insert(0, exp)

    tan = tk.Button(labelframe6, text='tan', command=tan, padx=5, pady=5, height=3, width=4, bg="wheat", fg="black")
    tan.pack(side=tk.LEFT, padx=3, pady=3)

play = True
while play:
    t_b()
    l_f_5()
    l_f_6()
    l_f_1()
    l_b_2()
    l_f_3()
    l_f_4()


    screen.mainloop()
screen.mainloop()