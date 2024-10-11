from functions import valid_password, replaceWithNumber, replaceWithSpecialNumber, replaceWithUpper, modify_password
def password(pword_user):
    pwd, wcontinue = valid_password(pwd=pword_user, show_warning=True)

    if wcontinue == False:
        print('The password is valid!')
        return pwd

    elif wcontinue == True:
        print("The password doesn't meet the requirements.")
        user_choice = input("Do you want to use a random password (r) or modify the existing password (m)? ")

        if user_choice.lower() == 'r':
            password2 = ""
            pwd2, wcontinue2 = valid_password(pwd=password2)

            while wcontinue2 == True:
                pwlength = random.randrange(10, 21)
                alphabet = "abcdefghijklmnopqrstuvwxyz"

                for j in range(pwlength):
                    next_letter_index = random.randrange(len(alphabet))
                    password2 = password2 + alphabet[next_letter_index]

                password2 = replaceWithNumber(password2, pwlength)
                password2 = replaceWithSpecialNumber(password2, pwlength)
                password2 = replaceWithUpper(password2, pwlength)

                password2, wcontinue2 = valid_password(pwd=password2)

            print('New password:', password2)
            return password2

        elif user_choice.lower() == 'm':
            pwd2 = modify_password(pword_user)
            print('Modified password:', pwd2)
            return pwd2
            # pwd2 = pword_user
            # print('TO DO Modified password: ')
            # return pwd2

        else:
            print("Invalid choice. Please try again.")
            return None
if __name__ == "__main__":
  pword_user = input('Enter your password: ')
  password(pword_user)
