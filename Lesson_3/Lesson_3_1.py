salary_list = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

mean_ = sum(salary_list)/len(salary_list)
print(f'Среднее арифметическое - {mean_}')

for i, j in enumerate(salary_list):
    salary_list[i] = (j - mean_) ** 2

var_ = sum(salary_list) / (len(salary_list))
var_ns = sum(salary_list) / (len(salary_list) - 1)

print(f'Дисперсия(смещенная оценка) - {var_}')
print(f'Дисперсия(несмещенная оценка) - {round(var_ns, 2)}')

print(f'Среднее квадратичное отклонение - {round(var_ns ** 0.5, 2)}')