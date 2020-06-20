"""

Hello! This is my solution for question 8

Hand calculations requires too much effort time time also, until reach %10^-4 true percent relative error.

Because of that I deciden to make necessary calculations with python. I am using Python 3.8

"""

c1 = 0
c2 = 0
c3 = 0
c1_list = [0]
c2_list = [0]
c3_list = [0]
tpre = 1
def calculations():
    global c1
    global c2
    global c3
    global tpre
    c1 = (3800 - ((-3)*(c2)) - ((-1)*(c3)))/15
    c2 = (1200 - ((-3)*(c1)) - ((-6)*(c3)))/18
    c3 = (2350 - ((-4)*(c1)) - ((-1)-(c2)))/12
    c1_list.append(c1)
    c2_list.append(c2)
    c3_list.append(c3)
    tpre = (c1_list[len(c1_list) -1] - c1_list[len(c1_list )- 2]) / c1_list[len(c1_list )- 1]
    print(tpre)
    # tpre = true percant relative error.
    return c1,c2,c3
iteration = 2
while True:
    calculations()
    print("\n{}. iteration:".format(iteration))
    if (tpre <= 10 ** -4):
        print("I reached targeted the true percent relative error which is {} at the {}. iteration".format(tpre,iteration))
        break
    else:
        iteration += 1
        continue






