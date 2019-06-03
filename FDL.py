import turtle
import sys

class Rule(object):
    
    def __init__(self, ileft, iright):
        self.left = ileft
        self.right = iright
    
    def apply(self,state):
        output = []
        for e in state:
            if e == self.left:
                output.append(self.right)
            else:
                output.append(e)
        return output



def flatten(state):
    output = []
    for i in state:
        #if type(i) == type(list()):  #This is unnecessary because strings are iterable
            for e in i:
                output.append(e)
        #else:
            #output.append(i)
    return output


def step(rules,state):
    test = state.copy()
    for i in rules:
        test = i.apply(test)
    return flatten(test)


def compute(depth,rules,start):
    if depth > 0:
        output = step(rules,start)
        a = compute(depth-1,rules,output)
        return a    #The function has to always return the next step
    else:           #otherwise depth 0 won't be returned
        return start

#r = list()
#r.append(Rule("F",["F","test"]))

#print(compute(5,r,["F"]))

def execute(turtle, length, cmd, args=None):
    if cmd == "scale" or cmd == "nop":
        if cmd == "scale":
            return length * float(args)
        if cmd == "nop":
            return length
    else:
        a = getattr(turtle,cmd)  #getattr finds the attribute that
        if args == None:         #matches the string given. if cmd = "fd" then
            args = length        #it will return the function turtle.fd
        a(float(args))
    return length

def parse(fdl):
   f = open(fdl)
   EOF = False
   rules = list()
   cmds = dict()
   while not EOF:
       a = f.readline().strip()
       if a == "":
           break
       a = a.split()

       if a[0] == "start":
           start = a[1:]
       if a[0] == "rule":
           rules.append( Rule(a[1],a[3:]) )
       if a[0] == "length":
           length = a[1]
       if a[0] == "depth":
           depth = a[1]
       if a[0] == "cmd":
           cmds[a[1]] = a[2:]
   return start, rules, length, depth, cmds

def run(turtle, fdl):
    start, rules, length, depth, cmds = parse(fdl)
    
    computed = compute(int(depth),rules,start)
    for i in computed:
        if len(cmds[i]) > 1:
            arg = cmds[i][1]
        else:
            arg = None
        length = execute(t, float(length), cmds[i][0], arg)



t = turtle.Turtle()
turtle.tracer(1000)
t.pu()
t.bk(200)
t.pd()

fdl = "snowflaske.fdl"
if len(sys.argv) > 1:    #A filename can be specified when running the script
    fdl = sys.argv[1]    #instead of changing the file

#cmds = dict()
#cmds["F"] = "fd"
#cmds["L"] = ["lt",60]
#cmds["R"] = ["rt",120]

#test = ["F","L","F","R","F","L","F"]

#start = ["F"]
#rules = list()
#rules.append(Rule("F",["F","L","F","R","F","L","F"]))

run(t, fdl)

turtle.update()
turtle.mainloop()