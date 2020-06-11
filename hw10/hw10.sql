

CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes WHERE height > min and height <= max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT d.name FROM dogs as d, parents as p, dogs as s WHERE d.name = p.child and s.name = p.parent ORDER BY s.height DESC ;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT p1.child AS sibling1, p2.child AS sibling2, d1.size AS size FROM parents as p1, parents as p2, size_of_dogs as d1, size_of_dogs as d2
       WHERE p1.parent = p2.parent AND p2.child > p1.child AND d1.name = p1.child AND d2.name = p2.child AND d1.size = d2.size;


-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT sibling1 || " and " || sibling2 || " are " || size || " siblings " FROM siblings;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(pogs, stack_height, last_height);

  INSERT INTO stacks_helper SELECT name , height, height FROM dogs ;
  INSERT INTO stacks_helper SELECT pogs || ", " || name , height + stack_height , height FROM stacks_helper, dogs
      WHERE height > last_height;
  INSERT INTO stacks_helper SELECT pogs || ", " || name , height + stack_height , height FROM stacks_helper, dogs
      WHERE height > last_height;
  INSERT INTO stacks_helper SELECT pogs || ", " || name , height + stack_height , height FROM stacks_helper, dogs
      WHERE height > last_height;

CREATE TABLE stacks AS
  SELECT pogs, stack_height FROM stacks_helper WHERE stack_height >= 170 ORDER BY stack_height ASC;


create table factorials as
    with fact(n, f) as (
       select 1, 1 UNION
       select n + 1, (n + 1) * f FROM fact WHERE n < 10
    )
    select f FROM fact;
