class SubfieldsinAI():
  def Subfields():
    print("Sub-Fields in AI are:")
    Lists=("Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing")
    for i in Lists:
        print(i)
    return
class OddEven():
  def Oddeven():
    num1=int(input("Enter the number:"))
    if num1%2==1:
        print("The number is ODD")
        message="Odd Number"
    else:
        print("The number is EVEN")
        message="Even Number"
        return message
class eligibility():
  def MarriageEligibility():
    gender=(input("Enter your Gender:"))
    age=int(input("Enter your Age:"))
    if((gender=="Male")&(age>=21)):
        print("Eligible for Marriage")
    elif((gender=="Female")&(age>=18)):
        print("Eligible for Marriage")
    else:
        print("Not eligible for Marriage")
    return
class tenthpercentage():
  def percentage():
    Sub1=int(input("Subject1="))
    Sub2=int(input("Subject2="))
    Sub3=int(input("Subject3="))
    Sub4=int(input("Subject4="))
    Sub5=int(input("Subject5="))
    add=Sub1+Sub2+Sub3+Sub4+Sub5
    print("Total=",add)
    Average=add/5
    print("Percentage:",Average)
    return
class triangleattributes():
  def Triangle():
    Height=int(input("Height:"))
    Breadth=int(input("Breadth"))
    print("Area Formula:(Height*Breadth)/2")
    Area=Height*Breadth/2
    print("Area of the Triangle:",Area)
    Height1=int(input("Height1:"))
    Height2=int(input("Height2:"))
    Breadth=int(input("Breadth:"))
    print("Perimeter formula:Height1+Height2+Breadth")
    Perimeter=Height1+Height2+Breadth
    print("Perimeter of the Triangle:",Perimeter)
    return
