"""
explanation:
    Goal is to get the emails and their matching line numbers out of a simple input text_file
    made possible by using: Regex, Enumerate, Argparse

created by Lior Tabibi
"""


import re
import argparse

def find_emails(name_of_txt_file): #creates the dict with valuable info
    regex = re.compile('[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+') #regex to find email
    try:
        with open(name_of_txt_file, 'r') as inputFile: #with-open file containing any text
            emails_from_file={} #empty dict to be filled with desired info
            for line_n, line in enumerate(inputFile,1): #enumerate to be used for getting the line numbers of each match
                success = regex.search(line)
                if success:
                    if success[0] in emails_from_file: #if key is already exists
                        if (type(emails_from_file[success[0]])) == list: #if key exists and already has 2 vals or more, then add the new val to the list (preventiog list of lists)
                            emails_from_file[success[0]].append(line_n)
                        else:
                            emails_from_file[success[0]] = [emails_from_file[success[0]], line_n]  #if key exists and already has a single val, then add the new val to the list
                    else:
                        emails_from_file[success[0]] = line_n
            return emails_from_file #dict of emails & line numbers
    except:
        print('please make sure filename is correct, that you`ve entered .txt and that the file is within the directory')
        main()


def arguments(): #checks if machine_readable or not
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("--machine", default=False, action="store_true") #if user executes the .py with flag = True, else = False
    args = parser.parse_args()

    if args.machine == True:
        return True
    else:
        return False


def main():
    name_of_txt_file = input('Please insert txt file_name (within the directory)')
    dict_of_emails=find_emails(name_of_txt_file)
    if arguments() == True:
        print ('Machine Readable format: textfile_name : line_number(s) : email_address')
        for key, val in dict_of_emails.items():
            print (name_of_txt_file, ':', val, ':', key)

    else:
        print ('Human Readable format: email_address:line number(s)')
        print (dict_of_emails)


if __name__== "__main__":
    main()
