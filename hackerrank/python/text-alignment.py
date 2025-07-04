#In Python, a string of text can be aligned left, right and center.
#.ljust(width)
#This method returns a left aligned string of length width.

# >>> width = 20
# >>> print 'HackerRank'.ljust(width,'-')
# HackerRank----------  

# .center(width)
# This method returns a centered string of length width.

# >>> width = 20
# >>> print 'HackerRank'.center(width,'-')
# -----HackerRank-----

# .rjust(width)
# This method returns a right aligned string of length width.

# >>> width = 20
# >>> print 'HackerRank'.rjust(width,'-')
# ----------HackerRank

# Task
# You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
# Your task is to replace the blank (______) with rjust, ljust or center.

# Input Format
# A single line containing the thickness value for the logo.
# Constraints
# The thickness must be an odd number.

# Output Format
# Output the desired logo.

# Sample Input
# 5

# Sample Output

#     H    
#    HHH   
#   HHHHH  
#  HHHHHHH 
# HHHHHHHHH
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHHHHHHHHHHHHHHHHHHHHHH   
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#   HHHHH               HHHHH             
#                     HHHHHHHHH 
#                      HHHHHHH  
#                       HHHHH   
#                        HHH    
#                         H 

# Solution

# Enter your code here. Read input from STDIN. Print output to STDOUT

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
#Explicación:
#Lo que se hace es imprimir un triangulo con el caracter 'H' con un tamaño de thickness. 
#La función rjust() se encarga de justificar el texto a la derecha, es decir, de agregar espacios a la izquierda del texto.
#La función ljust() se encarga de justificar el texto a la izquierda, es decir, de agregar espacios a la derecha del texto.
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))


#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    
# #Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

# #Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
    
# #Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
