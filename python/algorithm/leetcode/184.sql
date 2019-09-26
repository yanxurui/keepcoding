select Department.Name as Department, x.Name as Employee, x.Salary
from Employee x, Department
where x.DepartmentId = Department.Id and
Salary >= (select max(Salary) from Employee y where x.DepartmentId = y.DepartmentId);