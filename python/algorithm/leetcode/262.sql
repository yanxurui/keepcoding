select Request_at as Day,
round(sum(case when LOWER(Status) like 'cancelled%' then 1 else 0 end)/count(*), 2) as 'Cancellation Rate'
from Trips t
join Users u on t.Client_Id = u.Users_Id
and Banned = 'No'
where
Request_at between '2013-10-01' and '2013-10-03'
group by Request_at;