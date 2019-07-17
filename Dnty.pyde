global mouseX
global mouseY
global x
x = 0
selected = None
chars =[]
xfac = None
yfac = None
def keydown(Key):
    return(key == Key or key == Key.upper())
def setup():
    global tsize 
    tsize = 50    
cooldown = 100    

def draw():
    global cooldown
    global xfac
    global yfac
    global selected
    global x
    if x == 0:
        global mouseon
        def mouseon(x,y,xs,ys):
            return(mouseX <= xs and mouseX >= x and mouseY <= ys and mouseY >= y)
        class char:
            def __init__(self, name, HP, img, CLASS, SIZE, id):
                self.xp = 0
                self.yp = 0
                self.SIZE = SIZE
                self.name = name
                self.HP = HP
                self.img = img
                self.CLASS = CLASS
                self.id = id
                self.Hover = False
                chars.append(self)
        
        dog = char("john", 100, "x.png", "archer", 50, 0)
        print("l") 
        x = 2
        
    else:
        fill(255)
        background(255)
        stroke(0)
        strokeWeight(1)
        for i in range(height/50):
            for j in range(width/50):
                rect(i*50,j*50,49.5,49.5)
        for i in chars:
            if i.Hover:
                fill(0)
                rect(i.xp+1, i.yp+1, i.SIZE+1+i.xp/1000, i.SIZE+1+i.yp/1000)
            fill(0,255,0)
            strokeWeight(0)
            rect(i.xp, i.yp, i.SIZE, i.SIZE)
            stroke(127)
            strokeWeight(2)
            fill(0)
            textSize(10)
            textAlign(CENTER)
            text(str(i.HP), i.xp+i.SIZE/2,i.yp+i.SIZE+15)
            stroke(0)
        if mousePressed:
            for i in chars:
                if mouseon(i.xp,i.yp,i.xp+i.SIZE,i.yp+i.SIZE):
                    i.Hover = True
                    selected = i
                else:
                    i.Hover = False
        else:
            for i in chars:
                i.Hover = False
                selected = None
        if selected != None:
            leX = selected.xp
            leY = selected.yp
            if xfac == None:
                xfac = leX - mouseX
                yfac = leY - mouseY
            selected.xp = mouseX+xfac
            selected.yp = mouseY+yfac
            
        else:
            xfac = None
            yfac = None
        if keyPressed:
            if selected != None:
                if keydown('i'):
                    if cooldown == 0:
                        selected.HP += 10
                        print(selected.HP)
                        cooldown = 1
                elif keydown('k'):
                    if cooldown == 0:
                        selected.HP += -10
                        print(selected.HP)
                        cooldown = 1
                else:
                    cooldown = 0
        else:
            cooldown = 0
        

            
        
        
        
            

    
