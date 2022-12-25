# Project 1: Basic school administration tool
import csv

def write_into_csv(info_list):
    # ----> add data to new line every time
    with open('student_info.csv', 'a', newline='') as csv_file:
        # with open('student_info.csv', 'w+', newline='') as csv_file: ----> replace the entered data every time
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "Email-ID"])

        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_num = 1

    while (condition):
        student_info = input(
            "Enter student information for student #{} in the following formate (Name Age Contact_Number E-mail ID): ".format(student_num))
        #print(student_info, type(student_info))
        print("Entered Information: " + student_info)

        # split function
        student_info_list = student_info.split(' ')
        print("Entered split up information is: " + str(student_info_list))

        print("\nThe entered information is-\nName: {}\nAge: {}\nContact_Number: {}\nE-mail Id: {}".format(
            student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        choice_check = input("Is entered information correct? (yes/no): ")

        if choice_check == "yes":
            write_into_csv(student_info_list)

            condition_check = input(
                "Enter (yes/no) if you want to enter information for another student: ")
            if condition_check == "yes":
                condition = True
                student_num = student_num + 1
            elif condition_check == "no":
                condition = False
        elif choice_check == "no":
            print("\nPlease re-enter the values!")