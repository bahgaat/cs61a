.read lab12.sql

CREATE TABLE smallest_int_having AS
  SELECT time, smallest FROM students GROUP BY smallest HAVING count(smallest) = 1;

CREATE TABLE fa19favpets AS
  SELECT pet, count(*) as count FROM students GROUP BY pet ORDER BY count DESC LIMIT 10;


CREATE TABLE fa19dog AS
  SELECT pet, count(*) as count FROM students GROUP BY pet HAVING pet = 'dog';


CREATE TABLE obedienceimages AS
  SELECT seven, instructor, count(*) as count FROM students WHERE seven = '7'
      GROUP BY instructor ORDER BY instructor ASC;

create table pots as
    select 0 as place , 4 as value union
    select 1 , 20 union
    select 2 , 9 union
    select 3 , 3 union
    select 4 , 6 union
    select 5 , 2;
with
  paths ( path , last , total ) as (
    select value , place , value from pots as a union
    select path || ", " || b.path , b.last , total + b.last
        from paths as b
        where a.last - b.last > 1
  )
select path , max ( total ) from paths ;


create table ns as
   with t(n) as ( select 0 union select n+1 from t where n < 99 )
   select * from t;
create table ps as select n from ns where n > 0;
