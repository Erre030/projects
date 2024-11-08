
# description: validate emails (task specific: must not use re-library, but either validator-collection or validators libraries)

from validator_collection import validators

def main():
    print(check_mail(input("What's your email address?")))























def check_mail(s):

    try:
        email_address = validators.email(s)

        if email_address:
            return "Valid"

    except:
        return "Invalid"


if __name__ == "__main__":
    main()
