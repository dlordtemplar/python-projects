'''
In an Indian restaurant, the menu items are labeled with numbers, which the customers use to order their dishes.
Your job is to translate these numbers to the names of the dish for the cooks.

  1 Achari Paneer
  2 Gajar Ka Achar
  3 Aloo Dum
  4 Kabuli Chana 
  5 Baingan Bharta
  6 Apple Jalebi

Write a program that performs this task.

Sample output:

  Please enter the number of your dish:
  4
  Thank you for ordering Kabuli Chana.
'''
dishNames = {
    1:"Achari Paneer",
    2:"Gajar Ka Achar",
    3:"Aloo Dum",
    4:"Kabuli Chana",
    5:"Baingan Bharta",
    6:"Apple Jalebi"
}

def translateDishNumToName (dishNum):
    return dishNames[dishNum]

dishNum = int(input("Please enter the number of your dish:\n"))
dishName = translateDishNumToName(dishNum)
print("Thank you for ordering", dishName + ".")