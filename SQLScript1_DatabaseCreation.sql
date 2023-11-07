-- Assuming Oracle Database is installed on the machine
-- First, in Oracle database, CREATE a pluggable database named <WELBANK>
-- using DBCA (Database Configuration Assistant) or the pluggable creation script


-- Create user <welbank> in Pluggable Database <WELBANK>
create user welbank identified by 12345;
grant all privileges to welbank;

-- The tables will be created for user <welbank>
-- Connect to the <WELBANK> database with USER <welbank> to run the following script (using SQLPLUS, SQL Developer or any other tool)
-- conn welbank/12345@localhost:1521/welbank -- connection string using SQLPLUS

------------------- DATABASE CREATION SCRIPT -------------------

CREATE TABLE accounts (
    acc_id     NUMBER NOT NULL,
    acc_number NUMBER(13) NOT NULL,
    acc_bal    NUMBER(15, 2) NOT NULL,
    acc_type   VARCHAR2(10) NOT NULL,
    acc_start  DATE NOT NULL,
    acc_end    DATE,
    cus_id     NUMBER NOT NULL
);

ALTER TABLE accounts ADD CONSTRAINT accounts_pk PRIMARY KEY ( acc_id );

ALTER TABLE accounts ADD CONSTRAINT acc_number UNIQUE ( acc_number );

CREATE TABLE branches (
    brch_id     NUMBER NOT NULL,
    brch_name   VARCHAR2(35) NOT NULL,
    brch_phone  NUMBER(9) NOT NULL,
    brch_assets NUMBER(15) NOT NULL,
    reg_id      NUMBER NOT NULL
);

ALTER TABLE branches ADD CONSTRAINT branches_pk PRIMARY KEY ( brch_id );

CREATE TABLE cards (
    card_id     NUMBER NOT NULL,
    card_number NUMBER(16) NOT NULL,
    card_type   VARCHAR2(6) NOT NULL,
    card_limit  NUMBER(9, 2) NOT NULL,
    card_start  DATE NOT NULL,
    card_expiry DATE NOT NULL,
    card_status VARCHAR2(7) NOT NULL,
    acc_id      NUMBER NOT NULL
);

ALTER TABLE cards ADD CONSTRAINT cards_pk PRIMARY KEY ( card_id );

ALTER TABLE cards ADD CONSTRAINT card_number UNIQUE ( card_number );

CREATE TABLE customers (
    cus_id      NUMBER NOT NULL,
    nat_id      VARCHAR2(15) NOT NULL,
    cus_fn      VARCHAR2(35) NOT NULL,
    cus_ln      VARCHAR2(35) NOT NULL,
    gender      VARCHAR2(6) NOT NULL,
    cus_dob     DATE NOT NULL,
    nationality VARCHAR2(20),
    cus_email   VARCHAR2(35) NOT NULL,
    cus_phone   NUMBER(9) NOT NULL,
    occupation  VARCHAR2(50) NOT NULL,
    cus_addr    VARCHAR2(35) NOT NULL,
    brch_id     NUMBER NOT NULL,
    emp_id      NUMBER NOT NULL
);

ALTER TABLE customers ADD CONSTRAINT customers_pk PRIMARY KEY ( cus_id );

ALTER TABLE customers ADD CONSTRAINT nat_id UNIQUE ( nat_id );

CREATE TABLE departments (
    dep_id   NUMBER NOT NULL,
    dep_name VARCHAR2(35) NOT NULL
);

ALTER TABLE departments ADD CONSTRAINT departments_pk PRIMARY KEY ( dep_id );

CREATE TABLE employees (
    emp_id      NUMBER NOT NULL,
    emp_fn      VARCHAR2(15) NOT NULL,
    emp_ln      VARCHAR2(15) NOT NULL,
    gender      VARCHAR2(6) NOT NULL,
    nationality VARCHAR2(20) NOT NULL,
    emp_addr    VARCHAR2(35) NOT NULL,
    emp_email   VARCHAR2(35) NOT NULL,
    emp_phone   NUMBER(9) NOT NULL,
    emp_salary  NUMBER(9, 2) NOT NULL,
    hire_date   DATE NOT NULL,
    job_id      NUMBER NOT NULL,
    dep_id      NUMBER NOT NULL,
    brch_id     NUMBER NOT NULL
);

ALTER TABLE employees ADD CONSTRAINT employees_pk PRIMARY KEY ( emp_id );

CREATE TABLE jobs (
    job_id     NUMBER NOT NULL,
    job_title  VARCHAR2(35) NOT NULL,
    min_salary NUMBER(9) NOT NULL,
    max_salary NUMBER(9) NOT NULL,
    dep_id     NUMBER NOT NULL
);

ALTER TABLE jobs ADD CONSTRAINT jobs_pk PRIMARY KEY ( job_id );

CREATE TABLE loans (
    ln_id   NUMBER NOT NULL,
    ln_amt  NUMBER(12, 2) NOT NULL,
    ln_date DATE NOT NULL,
    cus_id  NUMBER NOT NULL
);

ALTER TABLE loans ADD CONSTRAINT loans_pk PRIMARY KEY ( ln_id );

CREATE TABLE loans_payment (
    lnpay_id      NUMBER NOT NULL,
    lnpay_amt     NUMBER(12, 2) NOT NULL,
    lnpay_rmn_amt NUMBER(12, 2) NOT NULL,
    lnpay_date    DATE NOT NULL,
    ln_id         NUMBER NOT NULL
);

ALTER TABLE loans_payment ADD CONSTRAINT loans_payment_pk PRIMARY KEY ( lnpay_id );

CREATE TABLE locations (
    loc_id    NUMBER NOT NULL,
    st_addr   VARCHAR2(35) NOT NULL,
    postcode  VARCHAR2(2) NOT NULL,
    digi_addr VARCHAR2(15) NOT NULL,
    brch_id   NUMBER NOT NULL,
    reg_id    NUMBER NOT NULL
);

CREATE UNIQUE INDEX locations__idx ON
    locations (
        brch_id
    ASC );

ALTER TABLE locations ADD CONSTRAINT locations_pk PRIMARY KEY ( loc_id );

CREATE TABLE regions (
    reg_id   NUMBER NOT NULL,
    reg_name VARCHAR2(35) NOT NULL
);

ALTER TABLE regions ADD CONSTRAINT regions_pk PRIMARY KEY ( reg_id );

CREATE TABLE transactions (
    txn_id      NUMBER NOT NULL,
    txn_type    VARCHAR2(15) NOT NULL,
    txn_date    DATE NOT NULL,
    txn_amount  NUMBER(15, 2) NOT NULL,
    txn_charges NUMBER(10, 2),
    acc_id      NUMBER NOT NULL,
    emp_id      NUMBER NOT NULL
);

ALTER TABLE transactions ADD CONSTRAINT transactions_pk PRIMARY KEY ( txn_id );

ALTER TABLE transactions
    ADD CONSTRAINT accounts_fk FOREIGN KEY ( acc_id )
        REFERENCES accounts ( acc_id );

ALTER TABLE cards
    ADD CONSTRAINT accounts_fkv1 FOREIGN KEY ( acc_id )
        REFERENCES accounts ( acc_id );

ALTER TABLE employees
    ADD CONSTRAINT branches_fkv1 FOREIGN KEY ( brch_id )
        REFERENCES branches ( brch_id );

ALTER TABLE locations
    ADD CONSTRAINT branches_fkv2 FOREIGN KEY ( brch_id )
        REFERENCES branches ( brch_id );

ALTER TABLE customers
    ADD CONSTRAINT branches_fkv3 FOREIGN KEY ( brch_id )
        REFERENCES branches ( brch_id );

ALTER TABLE loans
    ADD CONSTRAINT customers_fk FOREIGN KEY ( cus_id )
        REFERENCES customers ( cus_id );

ALTER TABLE accounts
    ADD CONSTRAINT customers_fkv2 FOREIGN KEY ( cus_id )
        REFERENCES customers ( cus_id );

ALTER TABLE employees
    ADD CONSTRAINT departments_fk FOREIGN KEY ( dep_id )
        REFERENCES departments ( dep_id );

ALTER TABLE transactions
    ADD CONSTRAINT employees_fkv4 FOREIGN KEY ( emp_id )
        REFERENCES employees ( emp_id );

ALTER TABLE customers
    ADD CONSTRAINT employees_fkv5 FOREIGN KEY ( emp_id )
        REFERENCES employees ( emp_id );

ALTER TABLE jobs
    ADD CONSTRAINT jobs_departments_fk FOREIGN KEY ( dep_id )
        REFERENCES departments ( dep_id );

ALTER TABLE employees
    ADD CONSTRAINT jobs_fk FOREIGN KEY ( job_id )
        REFERENCES jobs ( job_id );

ALTER TABLE loans_payment
    ADD CONSTRAINT loans_fk FOREIGN KEY ( ln_id )
        REFERENCES loans ( ln_id );

ALTER TABLE locations
    ADD CONSTRAINT regions_fk FOREIGN KEY ( reg_id )
        REFERENCES regions ( reg_id );

ALTER TABLE branches
    ADD CONSTRAINT regions_fkv2 FOREIGN KEY ( reg_id )
        REFERENCES regions ( reg_id );



-- SUMMARY
-- CREATE TABLE                            12
-- CREATE INDEX                             1
-- ALTER TABLE                             30

