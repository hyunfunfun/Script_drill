class Rectangle:
    def __init__(self,width=1, height=2):
        self.width=width
        self.height=height
    def getArea(self):
        return self.width*self.height
    def Perimeter(self):
        return (self.width+self.height)*2
    def Info(self):
        print('width:{0},height:{1},area:{2},perimeter:{3}'.format
              (self.width,self.height,self.getArea(),self.Perimeter()))



