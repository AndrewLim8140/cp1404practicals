# Imports
from datetime import *
from project import Project

# Constants
MENU = "(L)oad projects\n" \
       "(S)ave projects\n" \
       "(D)isplay projects\n" \
       "(F)ilter project by date\n" \
       "(A)dd new project\n" \
       "(U)pdate project\n" \
       "(Q)uit\n"
HEADER = 'Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n'

# Variables
project_name_length = 0
project_cost_length = 0
saved = False


def main(project_name_length, project_cost_length, saved):
    # Opening project.txt and ignoring header
    user_action = input(f"{MENU}>>>").upper()
    while user_action != 'Q':
        if user_action == 'L':
            file_name = input('\nEnter name of txt file without extention(.txt)\n'
                              '>>>')
            file_name = file_name + '.txt'
            try:
                in_file = open(file_name, 'r+')
            except FileNotFoundError:
                print('Inavlid txt name\n')
            else:
                # Remove header
                in_file.readline()

                projects = []
                for project in in_file:
                    project_parts = []
                    components = project.strip().split("\t")

                    # For alignment
                    if project_name_length < len(components[0]):
                        project_name_length = len(components[0])

                    if project_cost_length < len(components[3]):
                        project_cost_length = len(components[3])

                    project = Project(components[0], components[1], int(components[2]), float(components[3]),
                                      int(components[4]))

                    # Checkings if project is comleted and return boolean
                    iscompleted = project.is_completed()

                    projects.append(
                        [components[0], components[1], int(components[2]), float(components[3]), int(components[4]),
                         iscompleted])

                print(f'{file_name} loaded!\n')

        # Checking if a project.txt has been loaded
        # If not loaded request user to input valid txt
        try:
            projects[1]

        except UnboundLocalError:
            print("Please (L)oad a project txt file first to proceed\n")
            user_action = input(f"{MENU}>>>").upper()

        # If loaded continue
        else:
            # if user choose save
            if user_action == 'S':
                save_file = input('Enter name of txt file without extention(.txt)\n >>>')
                while save_file != file_name[:-4]:
                    print(f'Invalid txt file, please use the previously loaded file : {file_name}')
                    save_file=input('Enter name of txt file without extention(.txt)\n >>>')

                # Goes to the top of file
                in_file.seek(1)
                data = ''
                for project in projects:
                    data = data + project[0]+'\t'+project[1]+'\t'+str(project[2])+'\t'+str(project[3])+'\t'+str(project[4])+'\n'
                in_file.write(data)
                in_file.close()

                saved = True
                print()

            # If user chooses Display
            if user_action == 'D':
                # Sorting by priority then status of completion
                projects.sort(key=sort_priority, reverse=True)
                projects.sort(key=sort_completed_status)
                print("")

                for project in projects:
                    # Sample output :
                    # Organise Pantry, start: 20 / 07 / 2022, priority 1, estimate: $25.00, completion: 55 %
                    print(
                        f"{project[0]:<{project_name_length}}, start: {project[1]}, priority: {project[2]}, estimate: ${project[3]:<{project_cost_length}}, completion: {project[4]}%")
                print("")

            # If user chooses Filter
            if user_action == 'F':
                user_date = input("\n Show projects that start after date (DD/MM/YYYY) : ")
                print("")
                for project in projects:
                    #  comparing is user choosen date is more recent then saved date
                    date1 = Project('', project[1])
                    date2 = Project('', user_date)
                    date_test = date2 < date1

                    # if saved date is more recent then the user choosen date print project
                    if date_test:
                        print(
                            f"{project[0]:<{project_name_length}}, start: {project[1]}, priority: {project[2]}, estimate: ${project[3]:<{project_cost_length}}, completion: {project[4]}%")
                print("")

            # If user chooses add
            if user_action == 'A':
                new_name = input("Lets add a new project!\nName: ")

                # new_date = input("Start date (DD/MM/YYYY): ")
                new_date = str(date.today()).split('-')                 # date.today is given in YYYY-MM-DD thus we need
                new_date = new_date[2]+'/'+new_date[1]+'/'+new_date[0]  # to split then reorganise and add /

                # Loop to check if user inputted valid numbers
                parsed = 0  # increasing parsed to only loop at invalid inputs, ignoring previous valid
                while parsed != 3:
                    try:
                        if parsed < 1:
                            new_priority = int(input("Priority: "))
                            parsed = 1
                        if parsed < 2:
                            new_cost = int(input("Cost estimate: $"))
                            parsed = 2
                        new_percent = int(input("Completion percent :"))
                        parsed = 3
                    except ValueError:
                        print('Input valid number')

                # For alignment
                if project_name_length < len(new_name):
                    project_name_length = len(new_name)

                if project_cost_length < len(str(new_cost)):
                    project_cost_length = len(str(new_cost))

                # variable that shows completion as true if % == 100
                iscompleted = new_percent == 100
                print(iscompleted)

                projects.append([new_name,new_date,new_priority,new_cost,new_percent,iscompleted])
                print("")

            if user_action == 'U':
                counter = 0

                # Printing selections
                for project in projects:
                    print(f"{counter} {project[0]:<{project_name_length}}, start: {project[1]}, priority: {project[2]}, estimate: ${project[3]:<{project_cost_length}}, completion: {project[4]}%")
                    counter += 1

                # Acquiring user choice
                updating_project = int(input('Project choice: '))
                project = projects[updating_project]
                print(f"{project[0]:<{project_name_length}}, start: {project[1]}, priority: {project[2]}, estimate: ${project[3]:<{project_cost_length}}, completion: {project[4]}%")

                # User inputs
                new_percent = int(input('New percent: '))
                new_priority = int(input('New priority: '))

                # Changing old percent and priority
                project[4] = new_percent
                project[2] = new_priority

                # variable that shows completion as true if % == 100
                iscompleted = project[4] == '100'

                # appending new data to projects
                projects.append([project[0], project[1], project[2], project[3], project[4], iscompleted])

            user_action = input(f"{MENU}>>>").upper()

            if user_action == 'Q':
                if saved == True:
                    print('Thank you for using custom-built project management software')
                else:
                    warning=input('\nYou need to (S)ave before quitting else data will be lost\nAre you sure you want '
                                  'to quit? (Y/N)\n>>>').upper()
                    if warning == 'N':
                        user_action = ''
                        print("")
                    else:
                        saved = True
                        print('Thank you for using custom-built project management software')


def sort_completed_status(iterable):
    return iterable[5]


def sort_priority(iterable):
    return iterable[2]


main(project_name_length, project_cost_length, saved)
