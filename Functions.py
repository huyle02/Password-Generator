import random
def valid_password(pwd, show_warning=False):
    wlen = False
    if len(pwd) >= 10:
        wlen = True
    wupper_isupper = False
    wnumeric = False
    wspecial_number = False
    special_number = ["!", "?", "@", "#"]
    wcontinue = False

    for w in pwd:
        if w.isupper() == True:
            wupper_isupper = True
        if w in special_number:
            wspecial_number = True
        if w.isnumeric() == True:
            wnumeric = True

    if wlen == False:
        wcontinue = True
        if show_warning == True:
            print("Your password doesn't contain 10 words")
    if wspecial_number == False:
        wcontinue = True
        if show_warning == True:
            print("Your password doesn't contain a special number")
    if wnumeric == False:
        wcontinue = True
        if show_warning == True:
            print("Your password doesn't contain a number")
    if wupper_isupper == False:
        wcontinue = True
        if show_warning == True:
            print("Your password doesn't contain an upper case letter")

    return pwd, wcontinue

def replaceWithNumber(pwd, length_pwd):
    random_index = random.randrange(0, length_pwd)
    random_number = random.randrange(0, 9)
    return pwd[:(random_index)] + str(random_number) + pwd[(random_index + 1):]

def replaceWithSpecialNumber(pwd, length_pwd):
    special_number = ['!', '@', '#', '$']
    random_index = random.randrange(0, length_pwd)
    random_index_number = random.randrange(0, 4)
    return pwd[:(random_index)] + special_number[random_index_number] + pwd[(random_index + 1):]

def replaceWithUpper(pwd, length_pwd):
    random_index = random.randrange(0, length_pwd)
    return pwd[:(random_index)] + pwd[random_index].upper() + pwd[(random_index + 1):]

def modify_password(pwd):
  check1 = any(char.isdigit() for char in pwd)
  if check1 == False:
    pwd += str(random.randrange(0,10))
  check2 = any(char.isupper() for char in pwd)
  if check2 == False:
    pwd = pwd + random.choice("ABCD")
  check3 = any(char in ['!', '@', '#', '$'] for char in pwd)
  if check3 == False:
    pwd += random.choice(['!', '@', '#', '$'])
  return pwd
