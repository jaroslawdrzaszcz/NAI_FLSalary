"""
INPUT DATA:
Experience levels:
0 - no experience equals 0 p
0 - 2 year - low experience equals 1 p
2 - 5 years - medium experience equals 2 p
over 5 years - high experience equals 3 p

Education levels:
basic - 0 p
trade school - low experience equals 1 p
secondary school - medium experience equals 2 p
higher education - high experience equals 3 p

Work group levels:
very shy outsider - 0 p
outsider - 1 p
good work group cooperator - 2 p
excellent work group cooperator - 3 p

OUTPUT DATA:
Gross salary:
between 2400 - 5000 PLN
Gross salary sets:
low salary - 2400 - 3000 PLN
medium salary - 3000 - 4000 PLN
high_salary - 4000 - 5000 PLN

Rules:
IF no experience and basic education and  outsider THAN low salary
IF 1 year of experience and secondary school education and good work group worker group cooperator THAN medium salary
IF 6 years of experience and secondary school education and  excellent work group worker group cooperator THAN high salary
IF 3 years of experience and high school education and  good work group worker group cooperator THAN high salary
IF 4 years of experience and high school education and  very shy outsider THAN medium salary
"""

class Salary:
    experience = None
    work_group = None
    education_level = None
    engagement = None

    def salary_calculator_for_biedronka_cashier(self):
        if True:
            print ("dupa")


if __name__ == '__main__':
    Salary().education_level = 10
    Salary().work_group = 1
    Salary().education_level = 1

    Salary().salary_calculator()