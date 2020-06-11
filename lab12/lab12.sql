.read fa19data.sql

CREATE TABLE obedience AS
  SELECT seven, instructor FROM students;

CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 2 ORDER BY smallest LIMIT 20;


CREATE TABLE matchmaker AS
  SELECT Males.pet, Males.song, Males.color, Females.color
      FROM students as Males, students as Females
      WHERE Females.time > Males.time and Males.pet = Females.pet and Males.song = Females.song;
