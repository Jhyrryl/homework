-- 1. Execute DROP and CREATE commands
-- 2. Import csv files
-- 3. EXECUTE ALTER commands

DROP TABLE IF EXISTS Title;
DROP TABLE IF EXISTS Salary;
DROP TABLE IF EXISTS DepartmentManager;
DROP TABLE IF EXISTS EmployeeDepartment;
DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Department;

CREATE TABLE Department(
  dept_no CHAR(4) NOT NULL UNIQUE,
  dept_name VARCHAR(20) NOT NULL,
  PRIMARY KEY (dept_no)
);

CREATE TABLE Employee(
  emp_no INT NOT NULL UNIQUE,
  birth_date DATE NOT NULL,
  first_name VARCHAR(20) NOT NULL,
  last_name VARCHAR(20) NOT NULL,
  gender CHAR(1) NOT NULL,
  hire_date DATE NOT NULL,
  PRIMARY KEY (emp_no)
);

-- add primary key with SERIAL after data import
CREATE TABLE EmployeeDepartment(
  emp_no INT NOT NULL,
  dept_no VARCHAR(4) NOT NULL,
  from_date DATE NOT NULL,
  to_date DATE NOT NULL,
  FOREIGN KEY (emp_no) REFERENCES Employee(emp_no),
  FOREIGN KEY (dept_no) REFERENCES Department(dept_no)
);

-- add primary key with SERIAL after data import
CREATE TABLE DepartmentManager(
  dept_no VARCHAR(4) NOT NULL,
  emp_no INT NOT NULL,
  from_date DATE NOT NULL,
  to_date DATE NOT NULL,
  FOREIGN KEY (dept_no) REFERENCES Department(dept_no),
  FOREIGN KEY (emp_no) REFERENCES Employee(emp_no)
);

-- add primary key with SERIAL after data import
CREATE TABLE Salary(
  emp_no INT NOT NULL,
  salary INT NOT NULL,
  from_date DATE NOT NULL,
  to_date DATE NOT NULL,
  FOREIGN KEY (emp_no) REFERENCES Employee(emp_no)
);

-- add primary key with SERIAL after data import
CREATE TABLE Title(
  emp_no INT NOT NULL,
  title VARCHAR(30) NOT NULL,
  from_date DATE NOT NULL,
  to_date DATE NOT NULL,
  FOREIGN KEY (emp_no) REFERENCES Employee(emp_no)
);

-- Only execute the following
-- after csv files have been imported
ALTER TABLE Title
ADD id SERIAL;

ALTER TABLE Salary
ADD id SERIAL;

ALTER TABLE EmployeeDepartment
ADD id SERIAL;

ALTER TABLE DepartmentManager
ADD id SERIAL;