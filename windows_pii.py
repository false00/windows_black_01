#created by Citril, edited by false
#requires: pip install fake-factory
import sys
from faker import Factory
fake = Factory.create('en_US')


def main():
    console_output_to_file()
    for interation in range(1000):
        generate()


def console_output_to_file():
    sys.stdout = open('c:\customer_information.txt', 'w')


def generate():
#declaring variables for credit card
    prov = fake.credit_card_provider(card_type=None)
    num = fake.credit_card_number(card_type=None)
    sec = fake.credit_card_security_code(card_type=None)
    exp = fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")

    print ("Name: " + fake.name())
    print ("Employer: " + fake.company())
    print ("Position: " + fake.job())
    print ("Employee ID: " + fake.ean8())
    print ("Address: " + fake.address())
    print ("Credit Card: " + prov + " " + num + "\nCVV : " + sec + " " + exp)
    print ("SSN : " + fake.ssn())
    print ("----------------------")


if __name__ == "__main__": main()
