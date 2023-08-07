"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"
consolidated_data=[]
input_file = open(FILENAME)
def main():
    data = get_data()
    print(data)
    print(consolidated_data)
    assign_respective_class()

    input_file.close()



def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""

    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")

        consolidated_data.append(parts)


def assign_respective_class():
    number_of_class=len(consolidated_data)

    for line in range(0,number_of_class):
        class_code =consolidated_data[line][0]
        teacher_name=consolidated_data[line][1]
        total_student=consolidated_data[line][2]
        print("{cp} is taught by {teacher} and has {no_of_students} students".format(cp=class_code ,teacher=teacher_name ,no_of_students=total_student))

main()
