def inputdata():
        inputdata.name=input("Enter your name:")
        inputdata.address=input("Enter your address:")
        inputdata.cindate=input("Enter your check-in date:")
        inputdata.coutdate=input("Enter your check-out date:")
        print("Your room number:",101,"\n")

def roomrent():
        roomrent.s=0
        print ("We have the following rooms for you:-")

        print ("1.  Type A---->Rs.6000 PN\-")

        print ("2.  Type B---->Rs.5000 PN\-")

        print ("3.  Type C---->Rs.4000 PN\-")

        print ("4.  Type D---->Rs.3000 PN\-")

        x=int(input("Enter Your Choice Please->"))

        n=int(input("For How Many Nights Did You Stay:"))

        if(x==1):

            print ("You have opted room Type A")

            roomrent.s=6000*n

        elif (x==2):

            print ("You have opted room Type B")

            roomrent.s=5000*n

        elif (x==3):

            print ("You have opted room Type C")

            roomrent.s=4000*n

        elif (x==4):
            print ("You have opted room Type D")

            roomrent.s=3000*n

        else:

            print ("Please choose a room")

        print ("Your room rent is =",roomrent.s,"\n")

def res():
        res.r=0
        print("*****RESTAURANT MENU*****")

        print("1.Water----->Rs.20","2.tea----->Rs.10","3.Breakfast COMBO--->Rs.90","4.Lunch---->Rs.110","5.Dinner--->Rs.150","6.Exit")


        while (1):

            c=int(input("Enter your choice:"))


            if (c==1):
                d=int(input("Enter the quantity:"))
                res.r=res.r+20*d

            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 res.r=res.r+10*d

            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 res.r=res.r+90*d

            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 res.r=res.r+110*d

            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 res.r=res.r+160*d

            elif (c==6):
                break;
            else:
                print("Invalid Option")

        print ("Total food Cost = Rs",res.r,"\n")        

def	laundrybill():
        laundrybill.t=0
        print ("******LAUNDRY MENU*******")

        print ("1.Shorts----->Rs.3","2.Trousers----->Rs.4","3.Shirt--->Rs.5","4.Jeans---->Rs.6","5.Girlsuit--->Rs.8","6.Exit")

        while (1):

            e=int(input("Enter your choice:"))

            if (e==1):
                f=int(input("Enter the quantity:"))
                laundrybill.t=laundrybill.t+3*f

            elif (e==2):
                f=int(input("Enter the quantity:"))
                laundrybill.t=laundrybill.t+4*f

            elif (e==3):
                f=int(input("Enter the quantity:"))
                laundrybill.t=laundrybill.t+5*f

            elif (e==4):
                f=int(input("Enter the quantity:"))
                laundrybill.t=laundrybill.t+6*f

            elif (e==5):
                f=int(input("Enter the quantity:"))
                laundrybill.t=laundrybill.t+8*f
            elif (e==6):
                break;
            else:

                print ("Invalid option")


        print ("Total Laundary Cost=Rs",laundrybill.t,"\n")      

def display():
        a=200
        display.rt=0
        print ("******HOTEL BILL******")
        print ("Customer details:")
        print ("Customer name:",inputdata.name)
        print ("Customer address:",inputdata.address)
        print ("Check in date:",inputdata.cindate)
        print ("Check out date",inputdata.coutdate)
        
        print ("Your Room rent is:",roomrent.s)
        print ("Your Food bill is:",res.r)
        print ("Your laundary bill is:",laundrybill.t)
        

        display.rt=roomrent.s+res.r+laundrybill.t

        print ("Your sub total bill is:",display.rt)
        print ("Additional Service Charges is",a)
        print ("Your grandtotal bill is:",display.rt+a,"\n")
           

def menu():
    while (1):
        print("1.Enter Customer Data")
        
        print("2.Calculate rommrent")

        print("3.Calculate restaurant bill")

        print("4.Calculate laundry bill")

        print("5.Show Total Cost")

        print("6.EXIT")

        b=int(input("Enter your choice:"))
        if (b==1):
            inputdata()

        if (b==2):
            roomrent()

        if (b==3):
            res()

        if (b==4):
            laundrybill()

        if (b==5):
            display()

        if (b==6):
            quit()

menu()
    
