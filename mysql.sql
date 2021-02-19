
select name 
from animal_ins 
order by datetime
limit 1;

select count (distinct name) as count
from animal_ins;

select 
    NAME,
    count (distinct animal_id) as count
from animal_ins
group by name
having count (name) > 1
order by name;
