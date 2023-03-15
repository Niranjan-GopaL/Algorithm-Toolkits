class Cookie:
    def __init__(self,color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self,given_color):
        self.color = given_color


cookie1 = Cookie("red")
cookie1 = Cookie("blue")    

print(cookie1)