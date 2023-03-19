# a function that ensures the password has mix of all cases, numbers and special symbols
def check_password_strength():
    import re
    while True:     # this will keep prompting to the user until the user insert a password with all requirements
        print("for best security, create a password more than 8 characters containing,\n"
              "a mix lower and upper cases, digit(s), and special symbols eg  @,$,!,%,*,? or & ")
        password = input("create a strong password: ")
        if re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
            print("strong password")
            break
        else:
            print("weak password")
            continue

check_password_strength()
