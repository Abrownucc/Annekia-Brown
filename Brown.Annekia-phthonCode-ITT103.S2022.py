#FUNCTION calSalesAmt()
#salesAmt = (salesRecd * commRt + salesAmt)
#ENDFUNCTION
def calsalesAmt():
    global salesAmt
    salesAmt=(input(salesRecd * commRt + salesRecd))
                         
#WRITE "Please enter salesperson's full name"
#READ f_Name
f_Name=input("Please enter salesperson's full name ")

#WRITE "Please enter the salesRecd for the fornight)
#READ salesRecd
salesRecd=float(input("Please enter the salesRecd for the fornight "))

#WRITE "Please enters commission rate"
#READ commRt
        #calculation
        #commRt <= 1000)*0.06
        #commRt >= 1000 <2000) *0.07
        #commRt 2000 // >) * 0.1
        #commRt  1000) * 0.04
        #commRt  > 1000) * 0.0
commRt=float(input("Please enters commission rate "))

#WRITE "Please enters commission receivered"
#READ commRecd
commrecd=float(input("Please enters commission received "))

#SET count = 1
count=int(1)

#While count < 7 DO
while count < 3:
    calsalesAmt()
    print("The SalesAmt is", salesAmt)
#salesAmt <= 1000 THEN,  class = "1"|     
#salesAmt >= 1000 AND <= 2000 THEN,  class = "1" | 
#salesAmt == 2000 > THEN Class= "1"|   
#salesAmt < 1000  THEN, Class= "2"|
#salesAmt >=1000 THEN ,Class = "2"|
#salesAmt >= THEN, Class = "2"|
#salesAmt > 999 THEN,Class= "3"|
    
    #OTHERWISE WRITE " You have no commission for this fortnight Better luck next time"
    
    
    if salesRecd < 1000 or salesRecd == 1000:
        Class=("1")
        print("Class", Class)
    elif salesRecd > 1000 < 2000:
                Class= ("1")
                print("Class", Class)
    elif        salesRecd >2000 or salesRecd == 3000:
                   Class=("1")
                   print("Class", Class)
    elif           salesRecd < 1000 :
                      Class=("2")
                      print("Class", Class)
    elif              salesRecd > 1000:
                         Class=("2")
                         print("Class", Class)
    elif                 salesRecd < 900 :
                            Class=("3")
                            print("Class", Class)
    else:
                            print("You have no commission for this fortnight Better luck next time" )

    
#PRINT ""The salesperson", f_Name, "received commission of with a", salesAmt,"receiving  Class"
    print("The salesperson", f_Name, "received commission of with a",salesAmt ,"receiving  Class" )
    
    f_Name=input("Please enter salesperson's full name ")
    salesAmt=float(input("Please enter the salesAmt for the fornight "))
    commRt=float(input("Please enters commission rate "))
    commrecd=float(input("Please enters commission received "))

    count+=1
#ENDWHILE

print ("THIS PROGRAM IS COMPLETED")

                         
