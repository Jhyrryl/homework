-- List the following details of each employee:
-- 		employee number, last name, first name, gender, and salary.
select employee.emp_no, last_name, first_name, gender, salary
from employee
join salary on
employee.emp_no=salary.emp_no;

-- List employees who were hired in 1986.
select * from employee
where extract(year from hire_date)=1986;

-- List the manager of each department with the following information: 
-- 		department number, department name, the manager's employee number, 
-- 		last name, first name, and start and end employment dates.
select departmentmanager.dept_no, department.dept_name, departmentmanager.emp_no, 
	employee.last_name, employee.first_name, employee.hire_date, departmentmanager.to_date
from departmentmanager
left join employee on employee.emp_no=departmentmanager.emp_no
left join department on department.dept_no=departmentmanager.dept_no
where departmentmanager.to_date='9999-01-01';

-- List the department of each employee with the following information: 
-- 		employee number, last name, first name, and department name.
select employeedepartment.emp_no, employee.last_name, employee.first_name, department.dept_name
from employeedepartment
left join employee on employee.emp_no=employeedepartment.emp_no
left join department on department.dept_no=employeedepartment.dept_no;

-- List all employees whose first name is "Hercules" and last names begin with "B."
select first_name, last_name
from employee
where first_name='Hercules' and last_name like 'B%';

-- List all employees in the Sales department, including their:
-- 		employee number, last name, first name, and department name.
select employeedepartment.emp_no, last_name, first_name, department.dept_name
from employeedepartment
left join employee on employeedepartment.emp_no=employee.emp_no
left join department on employeedepartment.dept_no=department.dept_no
where employeedepartment.dept_no='d007';

-- List all employees in the Sales and Development departments, including their:
-- 		employee number, last name, first name, and department name.
select employeedepartment.emp_no, last_name, first_name, department.dept_name
from employeedepartment
left join employee on employeedepartment.emp_no=employee.emp_no
left join department on employeedepartment.dept_no=department.dept_no
where employeedepartment.dept_no='d007' or employeedepartment.dept_no='d005';

-- In descending order, list the frequency count of employee last names, 
-- 		i.e., how many employees share each last name.
select last_name, count(last_name) as freq_count
from employee
group by last_name
order by freq_count desc;