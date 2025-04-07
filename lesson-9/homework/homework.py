!pip install matplotlib

import matplotlib.pyplot as plt
import math
class Circl:
 def __init__(self,x,y,r):
  self.x=x
  self.y=y
  self.r=r

  
 def circles(self):
  circle = plt.Circle((0, 0), self.r, fill=False)  # Center at (0,0) and radius 5

  fig, ax = plt.subplots()
  ax.add_patch(circle)
  ax.set_xlim(-self.x, self.x)
  ax.set_ylim(-self.y, self.y)
  ax.set_aspect('equal') 
 def area(self):
  a=(self.r**2)*math.pi
  return a
 def perimeter(self):
  d=self.r*2*math.pi
  return d
import datetime as d

class Person:
    today = d.date.today()
    
    def __init__(self, name, country, *birth):
        self.name = name
        self.country = country
        self.birth_date = d.date(*birth)  # unpack tuple into date constructor

    def age(self):
        today = Person.today
        years = today.year - self.birth_date.year
        # Adjust if birthday hasn't occurred yet this year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            years -= 1
        return years

# Example usage
p = Person("Asror", "Uzbekistan", 2003, 4, 5)
print(p.age())  # Prints the current age
class Calculator:
    def __init__(self,*x):
        self.num=x
    def multiply(self):
        result=1
        for i in self.num:
            f=result*i
            result=f
        return result
    def add(self):
        result=0
        for i in self.num:
            f=result+i
            result=f
        return result
    def sub(self):
        result=self.num[0]
        for i in self.num[1:]:
           result-=i
        return result
    def division(self):
        result=self.num[0]
        for i in self.num[1:]:
          try:
            result/=i
          except ZeroDivisionError:
              return 'ZeroDivisionError'
        return result
#Write a Python program to create a class that represents a shape. Include methods to calculate its
#  area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.
class Triangle:
   def __init__(self,a,b,c):
      self.a=a if a<c+b else 0
      self.b=b if b<c+b else 0
      self.c=c if c<a+b else 0
   def shape(self): 
        
      pointA = (0, 0)
      pointB = (self.c, 0)
      pointC = (self.a, self.b)

      x = [pointA[0], pointB[0], pointC[0], pointA[0]]
      y = [pointA[1], pointB[1], pointC[1], pointA[1]]


      plt.figure()
      plt.plot(x, y, marker='o', color='blue')
      plt.fill(x, y, 'skyblue', alpha=0.5)
      plt.text(*pointA, 'A', fontsize=12, verticalalignment='top', horizontalalignment='right')
      plt.text(*pointB, 'B', fontsize=12, verticalalignment='top', horizontalalignment='left')
      plt.text(*pointC, 'C', fontsize=12, verticalalignment='bottom', horizontalalignment='center')

      plt.axis('equal')
      plt.grid(True)
      plt.title("Triangle ABC")
      plt.show()
   
      
