.read data.sql

-- QUESTIONS --



-------------------------------------------------------------------------
------------------------ Give Interest- ---------------------------------
-------------------------------------------------------------------------

UPDATE accounts SET amount = amount + 0.02 * amount;

CREATE TABLE bank_helper(name, amount);
    INSERT INTO bank_helper SELECT name || "'s" || " Checking account"  , amount / 2 FROM accounts;
    INSERT INTO bank_helper SELECT name || "'s" || " Savings account"  , amount / 2 FROM accounts;

create table give_interest_result as select * from accounts;-- just for tests

-------------------------------------------------------------------------
------------------------ Split Accounts ---------------------------------
-------------------------------------------------------------------------

DELETE FROM accounts;
INSERT INTO accounts(name, amount) SELECT name, amount FROM bank_helper;

create table split_account_results as select * from accounts; -- just for tests

-------------------------------------------------------------------------
-------------------------------- Whoops ---------------------------------
-------------------------------------------------------------------------
DROP table accounts;

CREATE TABLE average_prices AS
  SELECT category as category, AVG(MSRP) as average_price FROM products GROUP BY category;

CREATE TABLE lowest_prices AS
  SELECT store as store, item as item,MIN(price) as price FROM inventory GROUP BY item;

CREATE TABLE shopping_list AS
  SELECT name as name, store as store FROM products, lowest_prices WHERE item = name GROUP BY category HAVING MIN(MSRP / rating);

CREATE TABLE total_bandwidth AS
  SELECT SUM(Mbs) FROM stores as s1, shopping_list as s2 WHERE s1.store = s2.store;
