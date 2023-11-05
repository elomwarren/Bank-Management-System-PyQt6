-- WELBANK, Inc Database Administration

-- Connect to the pluggable <WELBANK> as sysdba

---------------------------------- CUSTOMER SERVICE employees

-- eg. Kwame Owusu
create user kwameowusu identified by 12345; -- CREATE CUSTOMER SERVICE department USER (as sysdba)
create user cs identified by 12345; -- general user of CUSTOMER SERVICE

-- GRANT NECESSARY PRIVILEGES TO USER
grant create session to kwameowusu; -- session creation privilege (as sysdba)
grant create session to cs;

-- GRANTING ACCESS to be done as USER <welbank>
-- Grant SELECT, INSERT, UPDATE privileges on CUSTOMERS related tables:
-- CUSTOMERS, ACCOUNTS, CARDS, TRANSACTIONS, LOANS, LOANS_PAYMENT

grant select, insert, update on welbank.CUSTOMERS to kwameowusu;
grant select, insert, update on welbank.ACCOUNTS to kwameowusu;
grant select, insert, update on welbank.CARDS to kwameowusu;
grant select, insert, update on welbank.TRANSACTIONS to kwameowusu;
grant select, insert, update on welbank.LOANS to kwameowusu;
grant select, insert, update on welbank.LOANS_PAYMENT to kwameowusu;

--
grant select, insert, update on welbank.CUSTOMERS to cs;
grant select, insert, update on welbank.ACCOUNTS to cs;
grant select, insert, update on welbank.CARDS to cs;
grant select, insert, update on welbank.TRANSACTIONS to cs;
grant select, insert, update on welbank.LOANS to cs;
grant select, insert, update on welbank.LOANS_PAYMENT to cs;

---------------------------------- HUMAN RESOURCES employees

-- eg. Kwadwo Hanson 
create user kwadwohanson identified by 12345; -- CREATE HUMAN RESOURCES department USER (as sysdba)
create user hr identified by 12345;

-- GRANT NECESSARY PRIVILEGES TO USER
grant create session to kwadwohanson;
grant create session to hr;

-- GRANTING ACCESS to be done as USER <welbank>
-- Grant SELECT, INSERT, UPDATE privileges on HR related tables:
-- EMPLOYEES, JOBS, DEPARTMENTS, BRANCHES, LOCATIONS, REGIONS

grant select, insert, update on welbank.EMPLOYEES to kwadwohanson;
grant select, insert, update on welbank.JOBS to kwadwohanson;
grant select, insert, update on welbank.DEPARTMENTS to kwadwohanson;
grant select, insert, update on welbank.BRANCHES to kwadwohanson;
grant select, insert, update on welbank.LOCATIONS to kwadwohanson;
grant select, insert, update on welbank.REGIONS to kwadwohanson;

--
grant select, insert, update on welbank.EMPLOYEES to hr;
grant select, insert, update on welbank.JOBS to hr;
grant select, insert, update on welbank.DEPARTMENTS to hr;
grant select, insert, update on welbank.BRANCHES to hr;
grant select, insert, update on welbank.LOCATIONS to hr;
grant select, insert, update on welbank.REGIONS to hr;

-- Tables Query format: select * from welbank.CUSTOMERS;