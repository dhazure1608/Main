def get_user():
       bank_name=input('Enter Bank Name\n')
       user_acc_dtls= {
             'HDFC':{'HDFC001':'HDFC_PWD_001',
                     'HDFC002':'HDFC_PWD_002',
                     'HDFC003':'HDFC_PWD_003'
                    },
             'ICICI':{'ICICI001':'ICICI_PWD_001',
                     'ICICI002':'ICICI_PWD_002',
                     'ICICI003':'ICICI_PWD_003'
                    },
             'KOTAK':{'KOTAK001':'KOTAK_PWD_001',
                     'KOTAK002':'KOTAK_PWD_002',
                     'KOTAK003':'KOTAK_PWD_003'
                    }
       }
       
       user_acc_balance= {
             'HDFC':{'HDFC001':20000,
                     'HDFC002':30000,
                     'HDFC003':40000
                    },
             'ICICI':{'ICICI001':20000,
                       'ICICI002':30000,
                      'ICICI003':40000
                     },
             'KOTAK':{'KOTAK001':20000,
                       'KOTAK002':30000,
                       'KOTAK003':40000
                     }
       }
       if bank_name in user_acc_dtls.keys():
            account_dtls=user_acc_dtls[bank_name]
            account_no=input('Enter Account Number\n')
            if account_no in account_dtls.keys():
                pwd = input('Enter Password\n')
                value=account_dtls[account_no]
                if pwd == value:
                    print ('Login Succesfull\n')
                    print('Welcome',account_no)
                    acc_user=user_acc_balance[bank_name]
                    acc_bal=acc_user[account_no]
                    user_choice=int(input('''Enter your options
                              1) Available Balance
                              2) Deposite
                              3) Withdrawn
                              '''))
                    if user_choice ==1:
                       print('Available Balance\n',acc_bal)
                    elif user_choice==2:
                       depo=int(input("Enter Deposite Amount\n"))
                       print('Available Balance\n',acc_bal+depo)
                    else:
                       withd=int(input("Enter Withdrawn Amount\n"))
                       print('Available Balance\n',acc_bal-withd)
                else:
                    print('Password is Invalid\n')
            else:
                print('Invalid User\n')
       else:
           print('Eneter Valid Bank Name')
       
print(get_user())
    
      
