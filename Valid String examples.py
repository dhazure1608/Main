pan_number=input('Eneter Pan Number\n')
if len(pan_number)==10 and pan_number.isalnum():
    if pan_number[0:5].isalpha() and pan_number[5:9].isdigit()and pan_number[9].isalpha():
        print('PAN NUMBER :',pan_number.upper())
    else:
        
        print('Enter Valid PAN Number')
else:
    print('Enter Full PAN Number')
