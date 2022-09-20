class Pile:
    def __init__(self):
        self.sticks=[]
        self.values=[]
    def apile(self,x,y):
        if self.sticks==[] and self.values==[]:
            self.sticks.append(x)
            self.values.append(y)
        elif x !=self.sticks[0] and y == self.values[0]-1:
            self.sticks.insert(0,x)
            self.values.insert(0,y)
        else:
            print("The card must be from a diferent stick and inmideatly lower")
    def show(self):
        if self.values==[] and self.sticks==[]:
            print("There is no cards")
        print(self.values, self.sticks)