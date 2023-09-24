from prac_06.programming_language import ProgrammingLanguage


python = ProgrammingLanguage('python', 'Dynamic', True, 1991)
ruby = ProgrammingLanguage('ruby', 'Dynamic', True, 1995)
visual_basic = ProgrammingLanguage('Visual Basic', 'Static', False, 1991)


print(python,'\n')
languages = [python , ruby , visual_basic]

print("The dynamically typed languages are :")
for language in languages:
    if language.is_dynamic() == True:
        print(language.language_name())

