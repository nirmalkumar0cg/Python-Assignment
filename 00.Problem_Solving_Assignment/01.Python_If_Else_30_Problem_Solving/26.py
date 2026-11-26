day = int(input('Enter The Date: '))
month = int(input('Enter The Month: '))
year = int(input('Enter The Year: '))

if month in [2]:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0):
        if day <= 29:
            print(day,'/',month,'/',year,'-> Valid')
    else:
        print(day,'/',month,'/',year,'-> Invalid')
            
if month in [4,6,9]:
    if day <= 30:
        print(day,'/',month,'/',year,'-> Valid')
    else:
        print(day,'/',month,'/',year,'-> Invalid') 
            
if month in [1,3,5,7,8,10,12]: # 1 3 5 7 8 10 12
    if day <= 31:
        print(day,'/',month,'/',year,'-> Valid')
    else:
        print(day,'/',month,'/',year,'-> Invalid')
if month >= 12:
    print(day,'/',month,'/',year,'-> Invalid')


    
    
        
    


            
                    
                
       
