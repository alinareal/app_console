example_string = 'vatrushekavetromoikamolodayanesnosnayale1012340656745' \
                 'nevozmognoevozmognominskayavodadkflkkllbbnvnnvf'

name_object = slice(0, 10)
surname_object = slice(10, 20)
patronymic_object = slice(20, 40)
age_object = slice(40, 43)
salary_object = slice(43, 53)
job_object = slice(53, 73)
free_text_object = slice(73, None)

name = example_string[name_object]
surname = example_string[surname_object]
patronymic = example_string[patronymic_object]
age = example_string[age_object]
salary = example_string[salary_object]
job = example_string[job_object]
free_text = example_string[free_text_object]

print(len(example_string))
print('Name: {}, length: {}'.format(name, len(name)))
print('Surname: {}, length: {}'.format(surname, len(surname)))
print('Patronymic: {}, length: {}'.format(patronymic, len(patronymic)))
print('Age: {}, length: {}'.format(age, len(age)))
print('Salary: {}, length: {}'.format(salary, len(salary)))
print('Job: {}, length: {}'.format(job, len(job)))
print('Free text: {}, length: {}'.format(free_text, len(free_text)))
