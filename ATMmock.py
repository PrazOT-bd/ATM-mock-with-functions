
import random
customers_database = {}
def init():

  print('Welcome to Bank of Kamazou')



  have_account = int(input('Do you have an account with us? 1(yes) 2(no) \n'))

  if(have_account == 1):
    login()

  elif(have_account == 2):
    register()

  else:
    print('You have selected an invalid option \n')
    init()
    
acc_balance = float(3000)

def register():
  print('**********Register********** \n')
  email = input('What is your email address? \n')
  global first_name
  first_name = input('What is your first name? \n')
  global last_name
  last_name = input('What is your last name? \n')
  password = input('Create a password for your account. \n')

  account_number = account_number_generator()

  user_details = [email, first_name, last_name, password]


  customers_database[account_number] = [first_name, last_name, email, password]

  print('Your account has been created.')
  print(' == ==== ==== ==== ==== ==== ==')
  print(f'This is your account number: {account_number}.')
  print(' == ==== ==== ==== ==== ==== == ')
  print('Make sure to keep it safe. \n')

  login()

def login():
  print('**********Login*********** \n')
  user_account_number = int(input('What is your account number? \n'))
  password = input('What is your password? \n')

  for account_number,user_details in customers_database.items():
    if account_number == user_account_number:
      if user_details[3] == password:
        bank_operations(user_details)

  print('Invalid account number or password')
  login()

def bank_operations(user):
  print(f'Dear {first_name} {last_name}. \n')
  selected_option = input('What would you like to do? (1)Deposit (2)Withdrawal (3)Complaints (4)Logout (5)Exit: ')
  try:
    selected_option = int(selected_option)
  except:
    print('Error, please try again')
    quit()
  
  if selected_option == 1:
    cash_deposit()

  elif selected_option == 2:
    withdrawal_ops()
  
  elif selected_option == 3:
    complaints()

  elif selected_option == 4:
    logout()

  elif selected_option == 5:
    exit()

  else:
    print('Invalid option selected.')
    bank_operations()


def withdrawal_ops():
  cash_amount = float(input('How much would you like to withdraw? '))
  if cash_amount > acc_balance:
    print('Insufficient funds. Please deposit into your account. \n')

  else:
    print(f'Please take your NGN{cash_amount} cash. \n')
    remaining_balance = acc_balance - cash_amount
    print(f'Your remaining balance is: NGN{remaining_balance}. \n')

  print('Thank you for banking with us.')
  exit()

def cash_deposit():
  deposit = float(input('How much would you like to deposit? '))
  current_balance = acc_balance + deposit
  print('Deposit was successfully...')
  print(f'You deposited NGN{deposit} into your account')
  print(f'Your account balance is NGN{current_balance} \n')
  print('Thank you for banking with us.')
  exit()


def complaints():
  complaint = str(input('What issue will you like to report? \n'))
  print('Thank you for contacting us. \n')
  print('your issues are being resolved. /n')
  print('Thank you for banking with us.')
  exit()


def account_number_generator():
  return random.randrange(1000000001,9999999999)

def logout():
  login()

init()