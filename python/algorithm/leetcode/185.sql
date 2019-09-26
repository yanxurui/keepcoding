select Department.Name as Department, x.Name as Employee, x.Salary
from Employee x, Department
where x.DepartmentId = Department.Id and
3 > (select count(distinct(Salary)) from Employee y where x.DepartmentId = y.DepartmentId and x.Salary<y.Salary)
order by Department, Salary desc;