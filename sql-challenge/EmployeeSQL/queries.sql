select employees.emp_no, last_name, first_name, gender, salary
from employees
join salaries on
employees.emp_no=salaries.emp_no;

select * from employees
where extract(year from hire_date)=1986;

select dept_manager.dept_no, departments.dept_name, dept_manager.emp_no, 
	employees.last_name, employees.first_name, employees.hire_date, dept_manager.to_date
from dept_manager
left join employees on employees.emp_no=dept_manager.emp_no
left join departments on departments.dept_no=dept_manager.dept_no
where dept_manager.to_date='9999-01-01';

select dept_emp.emp_no, employees.last_name, employees.first_name, departments.dept_name
from dept_emp
left join employees on employees.emp_no=dept_emp.emp_no
left join departments on departments.dept_no=dept_emp.dept_no;

select first_name, last_name
from employees
where first_name='Hercules' and last_name like 'B%';

select dept_emp.emp_no, last_name, first_name, departments.dept_name
from dept_emp
left join employees on dept_emp.emp_no=employees.emp_no
left join departments on dept_emp.dept_no=departments.dept_no
where dept_emp.dept_no='d007';

select dept_emp.emp_no, last_name, first_name, departments.dept_name
from dept_emp
left join employees on dept_emp.emp_no=employees.emp_no
left join departments on dept_emp.dept_no=departments.dept_no
where dept_emp.dept_no='d007' or dept_emp.dept_no='d005';

select last_name, count(last_name)
from employees
group by last_name;