import  interface
import work_file
import Controller as Con


def main():
	
	a = int(interface.show_menu())
	while a != 9:
		if a == 0:
			list  = work_file.Output_data_file_list('database.csv')
			[print(x) for x in list]
			input()
			a = interface.show_menu()
		if a == 1:
			name = input('Введите фамилию: ')
			lst = Con.find_employees_by_name(name)
			[print(lst[x]) for x in lst]
			input()
			a = interface.show_menu()

		elif a == 2:
			position = input('Введите должность: ')
			lst = Con.find_employees_by_position(position)
			[print(lst[x]) for x in lst]
			input()
			a = interface.show_menu()

		elif a == 3:
			Con.employees = Con.read_csv()
			lst = Con.find_employees_by_salary_range(Con.employees)
			for value in lst:
				print(value)
			input()
			a = interface.show_menu()

		elif a == 4:
			Con.employees = Con.read_csv()
			work_file.Input_data_file('database.csv', Con.add_line(), 'a')
			list = work_file.Output_data_file_list('database.csv')
			[print(x) for x in list]
			input()
			a = interface.show_menu()

		elif a == 5:
			data = input('Введите фамилию сотрудника, которого удалить: ')
			Con.remove_line(data)
			a = interface.show_menu()

		elif a == 6:
			Con.re_new()
			work_file.Output_data_file_list('database.csv')
			list = work_file.Output_data_file_list('database.csv')
			[print(x) for x in list]
			input()
			a = interface.show_menu()

		elif a == 7:
			Con.employees = Con.read_csv()
			Con.write_json(Con.employees)
			a = interface.show_menu()
			print(Con.read_json())
			input()
		elif a == 8:
			Con.write_csv(Con.employees)
			a = interface.show_menu()
			input()
		elif a == 9:
			a = interface.show_menu()
			quit()


main()