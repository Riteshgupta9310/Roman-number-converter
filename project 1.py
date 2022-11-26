def roman_numbers(num):
    print("Enter a number less than 400001")
    return
    value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    symbo["M","CM","D","CD","XC","L","XL","X","IX","V","IV","I"]    
    roman=""
    i=0
    while num>0:
        div=num//value[i]
        num=num%value[i]
        while div:
            roman=roman+symbol[i]
            div=div-1
        i+=1
    return roman

num=int(input("Enter an integer number:"))
print("roman numerals of",num,"is:",roman_numbers(num))



#PROJECT NO-17
#CONVERTER TO CONVERT GIVEN ROMAN TO INTEGER:-->
