-- DATA INPUT FOR THE BANKING SYSTEM

--  1.REGIONS TABLE --

insert all 
    into regions values (1, 'Greater Accra Region')
    into regions values (2, 'Ashanti Region')
    into regions values (3, 'Western Region')
    into regions values (4, 'Eastern Region')
    into regions values (5, 'Central Region')
    into regions values (6, 'Volta Region')
    into regions values (7, 'Northern Region')
    into regions values (8, 'Upper East Region')
    into regions values (9, 'Upper West Region')
    into regions values (10, 'Bono Region')
    into regions values (11, 'Bono East Region')
    into regions values (12, 'Ahafo Region')
    into regions values (13, 'Savannah Region')
    into regions values (14, 'North East Region')
    into regions values (15, 'Oti Region')
    into regions values (16, 'Western North Region')
select * from dual;

-- 2. BRANCHES TABLE DATA --

insert all 
    into branches values (1, 'East Legon', 550500217, 1500000000, 1)
    into branches values (5, 'Ho', 550500222, 1500000000, 6)
select * from dual; 

-- 3. LOCATIONS TABLE DATA --

insert all
    into locations values (1000, 'Lagos Avenue', 'GA', 'G4-378-7158', 1, 1)
    into locations values (1005, 'Ho Road', 'VH', 'VH-0079-1358',5, 6)
select * from dual;

-- 4. DEPARTMENTS TABLE DATA --

insert all
    into departments values (10, 'Customer service')
    into departments values (20, 'Operations')
    into departments values (30, 'Marketing')
    into departments values (40, 'Human resources')
    into departments values (50, 'Finance')
    into departments values (60, 'Information technology')
select * from dual;

-- 5. JOBS TABLE DATA --

insert all
    -- CUSTOMER SERVICE DEPARTMENT
    into jobs values (101, 'Bank teller', 25000, 45000, 10) -- 3 employees
    into jobs values (102, 'Personal banker', 35000, 65000, 10) -- 3 employees
    into jobs values (103, 'Customer service representative', 25000, 45000, 10) -- 2 employees
    into jobs values (104, 'Call center representative', 20000, 35000, 10) -- 2 employees   
    into jobs values (105, 'Account manager', 40000, 70000, 10) -- 1 employee
    into jobs values (106, 'Loan officer', 45000, 85000, 10) -- 1 employee
    into jobs values (107, 'Credit analyst', 40000, 70000, 10) -- 1 employees
    -- OPERATIONS DEPARTMENT
    into jobs values (201, 'Branch manager', 60000, 120000, 20) -- 1 employee
    into jobs values (202, 'Operations manager', 50000, 90000, 20) -- 1 employee
    into jobs values (203, 'Operations specialist', 35000, 65000, 20) -- 1 employee
    into jobs values (204, 'Teller supervisor', 40000, 70000, 20) -- 1 employee
    into jobs values (205, 'Loan processor', 35000, 65000, 20) -- 1 employee
    into jobs values (206, 'Compliance officer', 45000, 75000, 20) -- 1 employee
    into jobs values (207, 'IT support specialist', 30000, 50000, 20) -- 1 employee
    -- MARKETING DEPARTMENT
    into jobs values (301, 'Marketing manager', 65000, 125000, 30) -- 1 employee
    into jobs values (302, 'Marketing specialist', 45000, 85000, 30) -- 1 employee
    into jobs values (303, 'Product manager', 60000, 110000, 30) -- 1 employee
    into jobs values (304, 'Brand manager', 65000, 125000, 30) -- 1 employee
    into jobs values (305, 'Digital marketing manager', 50000, 90000, 30) -- 1 employee
    into jobs values (306, 'Social media manager', 40000, 70000, 30) -- 1 employee
    into jobs values (307, 'Public relations specialist', 45000, 75000, 30) -- 1 employee
    -- HUMAN RESOURCES DEPARTMENT
    into jobs values (401, 'Human resources manager', 75000, 150000, 40) -- 1 employee
    into jobs values (402, 'Recruiter', 50000, 90000, 40) -- 1 employee
    into jobs values (403, 'HR generalist', 45000, 75000, 40) -- 1 employee
    into jobs values (501, 'Financial analyst', 50000, 90000, 50) -- 1 employee
    into jobs values (502, 'Portfolio manager', 75000, 150000, 50) -- 1 employee
    into jobs values (503, 'Risk manager', 75000, 150000, 50) -- 1 employee
    into jobs values (504, 'Treasury manager', 85000, 175000, 50) -- 1 employee
    into jobs values (505, 'Controller', 95000, 195000, 50) -- 1 employee
    into jobs values (506, 'Chief financial officer (CFO)', 125000, 250000, 50) -- 1 employee
    -- INFORMATION TECHNOLOGY DEPARTMENT
    into jobs values (601, 'IT manager', 95000, 195000, 60) -- 1 employee
    into jobs values (602, 'Software engineer', 75000, 150000, 60) -- 1 employee
    into jobs values (603, 'Systems analyst', 65000, 125000, 60) -- 1 employee
    into jobs values (604, 'Database administrator', 65000, 125000, 60) -- 1 employee
    into jobs values (605, 'Network engineer', 75000, 150000, 60) -- 1 employee
    into jobs values (606, 'Security engineer', 85000, 175000, 60) -- 1 employee
select * from dual;

-- 6. EMPLOYEES TABLE DATA --

-- MODIFYING NLS_DATE_FORMAT TO ACCEPT THE DATE FORMAT USED IN THE INSERT STATEMENTS BELOW
-- ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD';

-- insert all the values in the list above into the employees table
insert all
    -- BRANCH 1: EAST LEGON
    -- CUSTOMER SERVICE dep x13
    -- BANK TELLERS 101 x3
    into employees values (1101001, 'Kwame', 'Owusu', 'Male', 'Ghanaian', 'East Legon', 'kwame.owusu@gmail.com', 550500216, 25000.00, '15-JUNE-20', 101, 10, 1)
    into employees values (1101002, 'Akosua', 'Appiah', 'Female', 'Ghanaian', 'East Legon', 'akosua.appiah@gmail.com', 502345678, 35000.00, '20-JUL-22', 101, 10, 1)
    into employees values (1101003, 'Kwesi', 'Annan', 'Male', 'Ghanaian', 'East Legon', 'kwesi.annan@gmail.com', 540345679, 37000.00, '12-AUG-19', 101, 10, 1)
    -- PERSONAL BANKERS 102 x3
    into employees values (1102001, 'Ama', 'Boateng', 'Female', 'Ghanaian', 'East Legon', 'ama.boateng@gmail.com', 248456789, 48000.00, '17-SEP-22', 102, 10, 1)
    into employees values (1102002, 'Kofi', 'Asante', 'Male', 'Ghanaian', 'East Legon', 'kofi.asante@gmail.com', 550567890, 50000.00, '25-OCT-21', 102, 10, 1)
    into employees values (1102003, 'Adwoa', 'Addo', 'Female', 'Ghanaian', 'East Legon', 'adwoa.addo@gmail.com', 550678901, 45000.00, '28-NOV-20', 102, 10, 1)
    -- CUSTOMER SERVICE REPRESENTATIVE 103 x2
    into employees values (1103001, 'Yaw', 'Amoah', 'Male', 'Ghanaian', 'East Legon', 'yaw.amoah@gmail.com', 570789012, 40000.00, '02-JAN-22', 103, 10, 1)
    into employees values (1103002, 'Abena', 'Acheampong', 'Female', 'Ghanaian', 'East Legon', 'abena.acheampong@gmail.com', 240890123, 45000.00, '08-FEB-20', 103, 10, 1)
    -- CALL CENTER REPRESENTATIVE 104 x2
    into employees values (1104001, 'Kwaku', 'Boakye', 'Male', 'Ghanaian', 'East Legon', 'kwaku.boakye@gmail.com', 548901234, 28000.00, '16-MAR-18', 104, 10, 1)
    into employees values (1104002, 'Akua', 'Dwomoh', 'Female', 'Ghanaian', 'East Legon', 'akua.dwomoh@gmail.com', 248012345, 29500.00, '21-APR-19', 104, 10, 1)
    -- ACCOUNT MANAGER 105 x1
    into employees values (1105001, 'Yaw', 'Frimpong', 'Male', 'Ghanaian', 'East Legon', 'yaw.frimpong@gmail.com', 597123456, 65000.00, '29-MAY-16', 105, 10, 1)
    -- LOAN OFFICER 106 x1
    into employees values (1106001, 'Adjoa', 'Gyan', 'Female', 'Ghanaian', 'East Legon', 'adjoa.gyan@gmail.com', 520234567, 85000.00, '03-JUL-18', 106, 10, 1)
    -- CREDIT ANALYST 107 x1
    into employees values(1107001, 'Kwabena', 'Kwame', 'Male', 'Ghanaian', 'East Legon', 'kwabena.kwame@gmail.com', 560345678, 70000.00, '09-AUG-15', 107, 10, 1)
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    -- OPERATIONS 20 x7
    -- BRANCH MANAGER 201 x1
    into employees values (1201001, 'Yaw', 'Osei', 'Male', 'Ghanaian', 'East Legon', 'yaw.osei@gmail.com', 552567890, 275000.00, '25-NOV-14', 201, 20, 1)
    -- OPERATIONS MANAGER 202 x1
    into employees values (1202001, 'Ama', 'Poku', 'Female', 'Ghanaian', 'East Legon', 'ama.poku@gmail.com', 553678901, 50000.00, '29-NOV-17', 202, 20, 1)
    -- OPERATIONS SPECIALIST 203 x1
    into employees values (1203001, 'Kwaku', 'Quansah', 'Male', 'Ghanaian', 'East Legon', 'kwaku.quansah@gmail.com', 250789012, 65000.00, '31-DEC-18', 203, 20, 1)
    -- TELLER SUPERVISOR 204 x1
    into employees values (1204001, 'Adwoa', 'Sarpong', 'Female', 'Ghanaian', 'East Legon', 'adwoa.sarpong@gmail.com', 250890123, 70000.00, '05-FEB-19', 204, 20, 1)
    -- LOAN PROCESSOR 205 x1
    into employees values (1205001, 'Yaw', 'Tetteh', 'Male', 'Ghanaian', 'East Legon', 'yaw.tetteh@gmail.com', 250901234, 65000.00, '11-FEB-20', 205, 20, 1)
    -- COMPLIANCE OFFICER 206 x1
    into employees values (1206001, 'Akosua', 'Yeboah', 'Female', 'Ghanaian', 'East Legon', 'akosua.yeboah@gmail.com', 550012345, 75000.00, '19-APR-19', 206, 20, 1)
    -- IT SUPPORT SPECIALIST 207 x1
    into employees values (1207001, 'Kwame', 'Agyei', 'Male', 'Ghanaian', 'East Legon', 'kwame.agyei@gmail.com', 553123456, 50000.00, '27-MAY-19', 207, 20, 1)
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    -- MARKETING 30 x7
    -- Marketing manager 301 x1
    into employees values (1301001, 'Abena', 'Ansah', 'Female', 'Ghanaian', 'Madina', 'abena.ansah@gmail.com', 521234567, 120000.00, '02-JUL-19', 301, 30, 1)
    -- Marketing specialist 302 x1
    into employees values (1302001, 'Kwadwo', 'Boateng', 'Male', 'Ghanaian', 'East Legon', 'kwadwo.boateng@gmail.com', 245345678, 77000.00, '09-AUG-21', 302, 30, 1)
    -- Product manager 303 x1
    into employees values (1303001, 'Adwoa', 'Cudjoe', 'Female', 'Ghanaian', 'Tema', 'adwoa.cudjoe@gmail.com', 245456789, 109000.00, '17-SEP-18', 303, 30, 1)
    -- Brand manager 304 x1
    into employees values (1304001, 'Kwaku', 'Danso', 'Male', 'Ghanaian', 'Ashaiman', 'kwaku.danso@gmail.com', 552267890, 112000.00, '25-OCT-17', 304, 30, 1)
    -- Digital marketing manager 305 x1
    into employees values (1305001, 'Adwoa', 'Egyir', 'Female', 'Ghanaian', 'East Legon', 'adwoa.egyir@gmail.com', 589678901, 81000.00, '29-NOV-18', 305, 30, 1)
    -- Social media manager 306 x1
    into employees values (1306001, 'Kwame', 'Frimpong', 'Male', 'Ghanaian', 'Adenta', 'kwame.frimpong@gmail.com', 256789012, 60000.00, '04-JAN-19', 306, 30, 1)
    -- Public relations specialist 307 x1
    into employees values (1307001, 'Abena', 'Gyamfi', 'Female', 'Ghanaian', 'East Legon', 'abena.gyamfi@gmail.com', 535890123, 67500.00, '11-FEB-19', 307, 30, 1)
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    -- HUMAN RESOURCES 40 x3
    -- HR manager 401 x1
    into employees values (1401001, 'Kwadwo', 'Hanson', 'Male', 'Ghanaian', 'East Legon', 'kwadwo.hanson@gmail.com', 248971234, 142700.00, '18-MAR-19', 401, 40, 1)
    -- Recruiter 402 x1
    into employees values (1402001, 'Joshua', 'Ayivor', 'Male', 'Ghanaian', 'East Legon', 'joshua.ayivor@gmail.com', 245012345, 67000.00, '26-APR-18', 402, 40, 1)
    -- HR generalist 403 x1
    into employees values (1403001, 'Fatima', 'Kone', 'Female', 'Ivorian', 'Madina Estate', 'fatima.kone@gmail.com', 545123456, 61700.00, '04-MAY-19', 403, 40, 1)
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    -- FINANCE 50 x6
    -- Financial Analyst 501 x1
    into employees values (1501001, 'Aisha', 'Bello','Female','Nigerian', 'East Legon', 'aisha.bello@gmail.com', 509682879, 85600.00, '12-JUN-19', 501, 50, 1)
    -- PortFolio manager 502 x1
    into employees values (1502001, 'Roch', 'Dankwa', 'Male', 'Ghanaian', 'East Legon', 'roch.dankwa@gmail.com', 509682879, 143000.00, '20-JUL-19', 502, 50, 1)
    -- Risk manager 503 x1
    into employees values (1503001, 'Richard', 'Asamoah', 'Male', 'Ghanaian', 'East Legon', 'richard.asamoah@gmail.com', 578682879, 145000.00, '28-AUG-19', 503, 50, 1)
    -- Treasury manager 504 x1
    into employees values (1504001,'Fausta', 'Amevor', 'Male', 'Ghanaian', 'East Legon', 'fausta.amevor@gmail.com', 509637752, 160000.00, '05-SEP-19', 504, 50, 1)
    -- Controller 505 x1
    into employees values (1505001, 'Emmanuel', 'Donkor', 'Male' , 'Ghanaian', 'East Legon', 'emmanuel.donkor@gmail.com', 587965410, 187000.00, '13-OCT-19', 505, 50, 1)
    -- Chief Financial Officer CFO 506 x1
    into employees values (1506001, 'David', 'Akuffo', 'Male', 'Ghanaian', 'East Legon', 'david.akuffo@gmail.com', 200634708, 242000.00, '21-NOV-19', 506, 50, 1)
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    -- INFORMATION TECHNOLOGY 60 x6
    -- IT manager 601 x1
    into employees values (1601001, 'Jessica', 'Annan', 'Female', 'Ghanaian', 'East Legon', 'jessica.annan@gmail.com', 285634708, 182000.00, '29-NOV-19', 601, 60, 1)
    -- Software Engineer 602 x1
    into employees values (1602001, 'Eunice', 'Asiedu', 'Female', 'Ghanaian', 'Spintex Road', 'eunice.asiedu@gmail.com', 502879752, 130000.00, '06-JAN-20', 602, 60, 1)
    -- System Analyst 603 x1
    into employees values (1603001, 'Samuel', 'Atsu', 'Male', 'Ghanaian', 'Osu', 'samuel.atsu@gmail.com', 213634708, 112500.00, '14-FEB-20', 603, 60, 1)
    -- Database Administrator 604 x1
    into employees values (1604001, 'Elorm', 'Kodjo', 'Male', 'Ghanaian', 'East Legon', 'elorm.kodjo@gmail.com', 509637752, 250000.00, '24-MAR-20', 604, 60, 1)
    -- Network engineer 605 x1
    into employees values (1605001, 'Caleb', 'Odom', 'Male', 'Ghanaian', 'East Legon', 'caleb.odom@gmail.com', 587965410, 125000.00, '01-APR-20', 605, 60, 1)
    -- Security engineer 606 x1
    into employees values (1606001, 'Winston', 'Kpadonou', 'Male', 'Beninois', 'Madina', 'winston.kpadonou@gmail.com', 200634708, 150000.00, '09-MAY-20', 606, 60, 1)
select * from dual;
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    -- BRANCH 5: HO --
INSERT ALL
    -- CUSTOMER SERVICE dep x13
    -- BANK TELLERS 101 x3
    INTO employees VALUES (5101001, 'Emmanuel', 'Duodu', 'Male', 'Ghanaian', 'Ho', 'emmanuel.duodu@gmail.com', 514441107, 25000.00, '15-JUN-20', 101, 10, 1)
    INTO employees VALUES (5101002, 'Emmanuella', 'Amenu', 'Female', 'Ghanaian', 'Ho', 'emmanuella.amenu@gmail.com', 200213472, 35000.00, '20-JUL-22', 101, 10, 1)
    INTO employees VALUES (5101003, 'Richmond', 'Amponsah', 'Male', 'Ghanaian', 'Ho', 'richmond.amponsah@gmail.com', 257567667, 37000.00, '12-AUG-19', 101, 10, 1)
    -- PERSONAL BANKERS 102 x3
    INTO employees VALUES (5102001, 'Caleb', 'Adom', 'Male', 'Ghanaian', 'Ho', 'caleb.adom@gmail.com', 284452196, 48000.00, '17-SEP-22', 102, 10, 1)
    INTO employees VALUES (5102002, 'Elvis', 'Adjei', 'Male', 'Ghanaian', 'Ho', 'elvis.adjei@gmail.com', 559894180, 50000.00, '25-OCT-21', 102, 10, 1)
    INTO employees VALUES (5102003, 'Francisca', 'Assan', 'Female', 'Ghanaian', 'Ho', 'francisca.assan@gmail.com', 225814496, 45000.00, '28-NOV-20', 102, 10, 1)
    -- CUSTOMER SERVICE REPRESENTATIVE 103 x2
    INTO employees VALUES (5103001, 'Winston', 'Akoto', 'Male', 'Ghanaian', 'Ho', 'winston.akoto@gmail.com', 297945138, 40000.00, '02-JAN-22', 103, 10, 1)
    INTO employees VALUES (5103002, 'Selina', 'Kwabea', 'Female', 'Ghanaian', 'Ho', 'selina.kwabea@gmail.com', 552685789, 45000.00, '08-FEB-20', 103, 10, 1)
    -- CALL CENTER REPRESENTATIVE 104 x2
    INTO employees VALUES (5104001, 'Jonathan', 'Nartey', 'Male', 'Ghanaian', 'Ho', 'jonathan.nartey@gmail.com', 223242522, 28000.00, '16-MAR-18', 104, 10, 1)
    INTO employees VALUES (5104002, 'Isaac', 'Nkansah', 'Male', 'Ghanaian', 'Ho', 'isaac.nkansah@gmail.com', 535943339, 29500.00, '21-APR-19', 104, 10, 1)
    -- ACCOUNT MANAGER 105 x1
    INTO employees VALUES (5105001, 'Esther', 'Dossou', 'Female', 'Beninois', 'Ho', 'esther.dossou@gmail.com', 564596587, 65000.00, '29-MAY-16', 105, 10, 1)
    -- LOAN OFFICER 106 x1
    INTO employees VALUES (5106001, 'Ruth', 'Tetteh', 'Female', 'Ghanaian', 'Ho', 'ruth.tetteh@gmail.com', 589435484, 85000.00, '03-JUL-18', 106, 10, 1)
    -- CREDIT ANALYST 107 x1
    INTO employees VALUES (5107001, 'Malika', 'Opoku', 'Female', 'Ghanaian', 'Ho', 'malika.opoku@gmail.com', 513894846, 70000.00, '09-AUG-15', 107, 10, 1)
    ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    -- OPERATIONS 20 x7
    -- BRANCH MANAGER 201 x1
    INTO employees VALUES (5201001, 'Lorreta', 'Kpeglo', 'Female', 'Ghanaian', 'Ho', 'lorreta.kpeglo@gmail.com', 256484547, 275000.00, '25-OCT-14', 201, 20, 1)
    -- OPERATIONS MANAGER 202 x1
    INTO employees VALUES (5202001, 'Randy', 'Amewu', 'Male', 'Ghanaian', 'Ho', 'randy.amewu@gmail.com', 248648474, 50000.00, '29-NOV-17', 202, 20, 1)
    -- OPERATIONS SPECIALIST 203 x1
    INTO employees VALUES (5203001, 'Stephen', 'Sefa', 'Female', 'Ghanaian', 'Ho', 'stephen.sefa@gmail.com', 265484748, 65000.00, '31-DEC-18', 203, 20, 1)
    -- TELLER SUPERVISOR 204 x1
    INTO employees VALUES (5204001, 'Daniel', 'Sagoe', 'Male', 'Ghanaian', 'Ho', 'daniel.sagoe@gmail.com', 541131418, 70000.00, '05-FEB-19', 204, 20, 1)
    -- LOAN PROCESSOR 205 x1
    INTO employees VALUES (5205001, 'Mabel', 'Abiah', 'Female', 'Ghanaian', 'Ho', 'mabel.abiah@gmail.com', 551874814, 65000.00, '11-MAR-20', 205, 20, 1)
    -- COMPLIANCE OFFICER 206 x1
    INTO employees VALUES (5206001, 'Jesse', 'Baffour', 'Male', 'Ghanaian', 'Ho', 'jesse.baffour@gmail.com', 564181964, 75000.00, '19-APR-19', 206, 20, 1)
    -- IT SUPPORT SPECIALIST 207 x1
    INTO employees VALUES (5207001, 'Eric', 'Narh', 'Male', 'Ghanaian', 'Ho', 'eric.narh@gmail.com', 586348112, 50000.00, '27-MAY-19', 207, 20, 1)
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    -- MARKETING 30 x7
    -- Marketing manager 301 x1
    INTO employees VALUES (5301001, 'Felicity', 'Anum', 'Female', 'Ghanaian', 'Ho', 'felicity.anum@gmail.com', 561984484, 120000.00, '02-JUL-19', 301, 30, 1)
    -- Marketing specialist 302 x1
    INTO employees VALUES (5302001, 'Ahmadou', 'Kourouma', 'Male', 'Ivorian', 'Ho', 'ahmadou.kourouma@gmail.com', 256859488, 77000.00, '09-AUG-21', 302, 30, 1)
    -- Product manager 303 x1
    INTO employees VALUES (5303001, 'Tasha', 'Mensah', 'Female', 'Ghanaian', 'Ho', 'tasha.mensah@gmail.com', 526181814, 109000.00, '17-SEP-18', 303, 30, 1)
    -- Brand manager 304 x1
    INTO employees VALUES (5304001, 'Deborah', 'Teye', 'Male', 'Ghanaian', 'Ho', 'deborah.teye@gmail.com', 514833333, 112000.00, '25-OCT-17', 304, 30, 1)
    -- Digital marketing manager 305 x1
    INTO employees VALUES (5305001, 'Amina', 'Bailly', 'Female', 'Ivorian', 'Ho', 'amina.bailly@gmail.com', 593518175, 81000.00, '29-NOV-18', 305, 30, 1)
    -- Social media manager 306 x1
    INTO employees VALUES (5306001, 'Mawuena', 'Gakpo', 'Male', 'Ghanaian', 'Ho', 'mawuena.gakpo@gmail.com', 267481681, 60000.00, '04-JAN-19', 306, 30, 1)
    -- Public relations specialist 307 x1
    INTO employees VALUES (5307001, 'Jeremy', 'Korateng', 'Male', 'Ghanaian', 'Ho', 'jeremy.korateng@gmail.com', 242618771, 67500.00, '11-FEB-19', 307, 30, 1)
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    -- HUMAN RESOURCES 40 x3
    -- HR manager 401 x1
    INTO employees VALUES (5401001, 'Kafui', 'Senou', 'Female', 'Ghanaian', 'Ho', 'kafui.senou@gmail.com', 542681167, 142700.00, '18-MAR-19', 401, 40, 1)
    -- Recruiter 402 x1
    INTO employees VALUES (5402001, 'Benjamin', 'Agbavor', 'Male', 'Ghanaian', 'Ho', 'benjamin.agbavor@gmail.com', 256168117, 67000.00, '26-APR-18', 402, 40, 1)
    -- HR generalist 403 x1
    INTO employees VALUES (5403001, 'Hanna', 'Akko', 'Female', 'Ghanaian', 'Ho', 'hanna.akko@gmail.com', 248628146, 61700.00, '04-MAY-19', 403, 40, 1)
    ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    -- FINANCE 50 x6
    -- Financial Analyst 501 x1
    INTO employees VALUES (5501001, 'Pearl', 'Kumi', 'Female', 'Ghanaian', 'Ho', 'pearl.kumi@gmail.com', 524681817, 85600.00, '12-JUN-19', 501, 50, 1)
    -- PortFolio manager 502 x1
    INTO employees VALUES (5502001, 'Olivia', 'Boafo', 'Female', 'Ghanaian', 'Ho', 'olivia.boafo@gmail.com', 241565571, 143000.00, '20-JUL-19', 502, 50, 1)
    -- Risk manager 503 x1
    INTO employees VALUES (5503001, 'Henry', 'Agawu', 'Male', 'Ghanaian', 'Ho', 'henry.agawu@gmail.com', 245618918, 145000.00, '28-AUG-19', 503, 50, 1)
    -- Treasury manager 504 x1
    INTO employees VALUES (5504001, 'Bismark', 'Adjahoe', 'Male', 'Ghanaian', 'Ho', 'bismark.adjahoe@gmail.com', 247818171, 160000.00, '05-SEP-19', 504, 50, 1)
    -- Controller 505 x1
    INTO employees VALUES (5505001, 'Esther', 'Adu', 'Female', 'Ghanaian', 'Ho', 'esther.adu@gmail.com', 512482797, 187000.00, '13-OCT-19', 505, 50, 1)
    -- Chief Financial Officer CFO 506 x1
    INTO employees VALUES (5506001, 'Shadrack', 'Agbenu', 'Male', 'Ghanaian', 'Ho', 'shadrack.agbenu@gmail.com', 240427178, 242000.00, '21-NOV-19', 506, 50, 1)
    -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    -- INFORMATION TECHNOLOGY 60 x6
    -- IT manager 601 x1
    INTO employees VALUES (5601001, 'Regis', 'Agbo', 'Male', 'Beninois', 'Ho', 'regis.agbo@gmail.com', 248926184, 182000.00, '29-NOV-19', 601, 60, 1)
    -- Software Engineer 602 x1
    INTO employees VALUES (5602001, 'Emmanuel', 'Adofo', 'Male', 'Ghanaian', 'Ho', 'emmanuel.adofo@gmail.com', 269587752, 130000.00, '06-JAN-20', 602, 60, 1)
    -- System Analyst 603 x1
    INTO employees VALUES (5603001, 'Abubakar', 'Yusif', 'Male', 'Ghanaian', 'Ho', 'abubakar.yusif@gmail.com', 563657774, 112500.00, '14-FEB-20', 603, 60, 1)
    -- Database Administrator 604 x1
    INTO employees VALUES (5604001, 'Gloria', 'Zigah', 'Female', 'Ghanaian', 'Ho', 'gloria.zigah@gmail.com', 548981878, 250000.00, '24-MAR-20', 604, 60, 1)
    -- Network engineer 605 x1
    INTO employees VALUES (5605001, 'Joana', 'Twasam', 'Female', 'Ghanaian', 'Ho', 'joana.twasam@gmail.com', 536818787, 125000.00, '01-APR-20', 605, 60, 1)
    -- Security engineer 606 x1
    INTO employees VALUES (5606001, 'Jacqueline', 'Thompson', 'Female', 'Ghanaian', 'Ho', 'jacqueline.thompson@gmail.com', 251816871, 150000.00, '09-MAY-20', 606, 60, 1)
SELECT * FROM dual;


-- 8. CUSTOMERS TABLE --

-- DATA INSERTION
-- EAST LEGON CUSTOMERS

insert all
    into customers values (10000001, 'GHA-000000001-0', 'Kwame', 'Anane', 'Male', '25-JUL-80', 'Ghanaian', 'kwame.anane@gmail.com', 502345678, 'Accountant', 'Madina', 1, 1102001)
    into customers values (10000002, 'GHA-000000002-0', 'James', 'Boateng', 'Male', '30-MAY-90', 'Ghanaian', 'james.boateng@gmail.com', 502345679, 'Architect', 'East Legon', 1, 1102002)
    into customers values (10000003, 'GHA-000000003-0', 'Sarah', 'Adjei', 'Female', '15-JUN-95', 'Ghanaian', 'sarah.adjei@gmail.com', 502345680, 'Software Engineer', 'Botwe', 1, 1102003)
    into customers values (10000004, 'GHA-000000004-0', 'Adwoa', 'Mensah', 'Female', '20-SEP-88', 'Ghanaian', 'adwoa.mensah@gmail.com', 502345681, 'Lawyer', 'Adenta', 1, 1102001)
    into customers values (10000005, 'GHA-000000005-0', 'Yaw', 'Osei', 'Male', '28-DEC-75', 'Ghanaian', 'yaw.osei@gmail.com', 502345682, 'Journalist', 'Tema', 1, 1102002)
    into customers values (10000006, 'GHA-000000006-0', 'Ama', 'Nyarko', 'Female', '05-NOV-83', 'Ghanaian', 'ama.nyarko@gmail.com', 502345683, 'Nurse', 'Ashaiman', 1, 1102003)
    into customers values (10000007, 'GHA-000000007-0', 'Kwabena', 'Appiah', 'Male', '15-MAR-92', 'Ghanaian', 'kwabena.appiah@gmail.com', 502345684, 'Physician', 'Osu', 1, 1102001)
    into customers values (10000008, 'GHA-000000008-0', 'Linda', 'Quansah', 'Female', '19-OCT-78', 'Ghanaian', 'linda.quansah@gmail.com', 502345685, 'Teacher', 'Dansoman', 1, 1102002)
    into customers values (10000009, 'GHA-000000009-0', 'Kojo', 'Acheampong', 'Male', '23-JAN-85', 'Ghanaian', 'kojo.acheampong@gmail.com', 502345686, 'School Teacher', 'Madina', 1, 1102003)
    into customers values (10000010, 'GHA-000000010-0', 'Abena', 'Frimpong', 'Female', '14-AUG-82', 'Ghanaian', 'abena.frimpong@gmail.com', 502345687,'Police Officer', 'East Legon', 1, 1102001)
    into customers values (10000011, 'GHA-000000011-0', 'Yaw', 'Asare', 'Male', '17-FEB-79', 'Ghanaian', 'yaw.asare@gmail.com', 502345688, 'Statistician', 'Botwe', 1, 1102002)
    into customers values (10000012, 'GHA-000000012-0', 'Aba', 'Kwakye', 'Female', '29-MAY-81', 'Ghanaian', 'aba.kwakye@gmail.com', 502345689, 'Surgeon', 'Adenta', 1, 1102003)
    into customers values (10000013, 'GHA-000000013-0', 'Kwasi', 'Agyei', 'Male', '01-APR-77', 'Ghanaian', 'kwasi.agyei@gmail.com', 502345690, 'Data Scientist', 'Tema', 1, 1102001)
    into customers values (10000014, 'GHA-000000014-0', 'Esi', 'Owusu', 'Female', '15-JUL-99', 'Ghanaian', 'esi.owusu@gmail.com', 502345691, 'Web Developer', 'Ashaiman', 1, 1102002)
    into customers values (10000015, 'GHA-000000015-0', 'Kojo', 'Antwi', 'Male', '30-JUN-86', 'Ghanaian', 'kojo.antwi@gmail.com', 502345692, 'Software Engineer', 'Osu', 1, 1102003)
    into customers values (10000016, 'GHA-000000016-0', 'Afia', 'Kumi', 'Female', '02-SEP-89', 'Ghanaian', 'afia.kumi@gmail.com', 502345693, 'School Teacher', 'Dansoman', 1, 1102001)
    into customers values (10000017, 'GHA-000000017-0', 'Yaw', 'Nkansah', 'Male', '18-NOV-76', 'Ghanaian', 'yaw.nkansah@gmail.com', 502345694, 'Pharmacist', 'Madina', 1, 1102002)
    into customers values (10000018, 'GHA-000000018-0', 'Ama', 'Yeboah', 'Female', '04-DEC-84', 'Ghanaian', 'ama.yeboah@gmail.com', 502345695, 'Lawyer', 'East Legon', 1, 1102003)
    into customers values (10000019, 'GHA-000000019-0', 'Kwabena', 'Gyamfi', 'Male', '28-FEB-80', 'Ghanaian', 'kwabena.gyamfi@gmail.com', 502345696, 'Graphic Designer', 'Botwe', 1, 1102001)
    into customers values (10000020, 'GHA-000000020-0', 'Akosua', 'Ofori', 'Female', '12-APR-97', 'Ghanaian', 'akosua.ofori@gmail.com', 502345697, 'Journalist', 'Adenta', 1, 1102002)
    into customers values (10000021, 'GHA-000000021-0', 'Thomas', 'Darko', 'Male', '16-MAR-83', 'Ghanaian', 'thomas.darko@gmail.com', 502345698, 'Accountant', 'Tema', 1, 1102003)
    into customers values (10000022, 'GHA-000000022-0', 'Adwoa', 'Sarpong', 'Female', '07-MAY-98', 'Ghanaian', 'adwoa.sarpong@gmail.com', 502345699, 'Actuary', 'Ashaiman', 1, 1102001)
    into customers values (10000023, 'GHA-000000023-0', 'Kwame', 'Adom', 'Male', '24-JUL-78', 'Ghanaian', 'kwame.adom@gmail.com', 502345700, 'Statistician', 'Osu', 1, 1102002)
    into customers values (10000024, 'GHA-000000024-0', 'Efia', 'Amoah', 'Female', '08-AUG-96', 'Ghanaian', 'efia.amoah@gmail.com', 502345701, 'Economist', 'Dansoman', 1, 1102003)
    into customers values (10000025, 'GHA-000000025-0', 'Yaw', 'Opoku', 'Male', '30-SEP-87', 'Ghanaian', 'yaw.opoku@gmail.com', 502345702, 'Actuary', 'Madina', 1, 1102001)
    into customers values (10000026, 'GHA-000000026-0', 'Abena', 'Adu', 'Female', '16-OCT-99', 'Ghanaian', 'abena.adu@gmail.com', 502345703, 'Nurse', 'East Legon', 1, 1102002)
    into customers values (10000027, 'GHA-000000027-0', 'Kojo', 'Twumasi', 'Male', '02-NOV-79', 'Ghanaian', 'kojo.twumasi@gmail.com', 502345704, 'Data Engineer', 'Botwe', 1, 1102003)
    into customers values (10000028, 'GHA-000000028-0', 'Akua', 'Asamoah', 'Female', '19-DEC-81', 'Ghanaian', 'akua.asamoah@gmail.com', 502345705, 'Civil Servant', 'Adenta', 1, 1102001)
    into customers values (10000029, 'GHA-000000029-0', 'Kwabena', 'Owusu-Ansah', 'Male', '05-JAN-82', 'Ghanaian', 'kwabena.owusuansah@gmail.com', 502345706,  'Librarian','Tema', 1, 1102002)
    into customers values (10000030, 'GHA-000000030-0', 'Afia', 'Osei-Tutu', 'Female', '21-FEB-98', 'Ghanaian', 'afia.oseitutu@gmail.com', 502345707, 'Police Officer', 'Ashaiman', 1, 1102003)
select * from dual;


-- HO CUSTOMERS

insert all
    into customers values (50000001, 'GHA-000000031-0', 'James', 'Abu', 'Male', '02-MAY-88', 'Ghanaian', 'james.abu@gmail.com', 502123456, 'Statistician', 'Kpeve', 5, 5102001)
    into customers values (50000002, 'GHA-000000032-0', 'Abigail', 'Essuman', 'Female', '10-MAR-89', 'Ghanaian', 'abigail.essuman@gmail.com', 203123457, 'Police Officer','Akatsi', 5, 5102002)
    into customers values (50000003, 'GHA-000000033-0', 'Michael', 'Amewu', 'Male', '21-JUL-86', 'Ghanaian', 'michael.amewu@gmail.com', 505123458, 'Electrician', 'Asikuma', 5, 5102003)
    into customers values (50000004, 'GHA-000000034-0', 'Sarah', 'Biney', 'Female', '30-NOV-83', 'Ghanaian', 'sarah.biney@gmail.com', 205123459, 'Software Developer', 'Amedzofe', 5, 5102001)
    into customers values (50000005, 'GHA-000000035-0', 'Samuel', 'Dadzie', 'Male', '15-DEC-95', 'Ghanaian', 'samuel.dadzie@gmail.com', 502123450, 'Lawyer', 'Donkorkrom', 5, 5102002)
    into customers values (50000006, 'GHA-000000036-0', 'Grace', 'Boadu', 'Female', '05-JUN-90', 'Ghanaian', 'grace.boadu@gmail.com', 205123461, 'Nurse', 'Hohoe', 5, 5102003)
    into customers values (50000007, 'GHA-000000037-0', 'Benjamin', 'Dogbey', 'Male', '20-JAN-81', 'Ghanaian', 'benjamin.dogbey@gmail.com', 502123462, 'Lawyer', 'Akosombo', 5, 5102001)
    into customers values (50000008, 'GHA-000000038-0', 'Elizabeth', 'Badu', 'Female', '07-APR-97', 'Ghanaian', 'elizabeth.badu@gmail.com', 205123463, 'Dentist', 'Kpeve', 5, 5102002)
    into customers values (50000009, 'GHA-000000039-0', 'Joseph', 'Gadebgeku', 'Male', '27-FEB-82', 'Ghanaian', 'joseph.gadebgeku@gmail.com', 502123464, 'Doctor','Akatsi', 5, 5102003)
    into customers values (50000010, 'GHA-000000040-0', 'Rita', 'Barnes', 'Female', '15-SEP-99', 'Ghanaian', 'rita.barnes@gmail.com', 205123465, 'Financial Analyst', 'Asikuma', 5, 5102001)
    into customers values (50000011, 'GHA-000000041-0', 'Paul', 'Abaane', 'Male', '22-APR-79', 'Ghanaian', 'paul.abaane@gmail.com', 502123466, 'Marketing Manager', 'Amedzofe', 5, 5102002)
    into customers values (50000012, 'GHA-000000042-0', 'Esther', 'Baffour', 'Female', '03-JUL-94', 'Ghanaian', 'esther.baffour@gmail.com', 205123467, 'Accountant', 'Donkorkrom', 5, 5102003)
    into customers values (50000013, 'GHA-000000043-0', 'Peter', 'Abakah', 'Male', '28-NOV-82', 'Ghanaian', 'peter.abakah@gmail.com', 502123468, 'Farmer', 'Hohoe', 5, 5102001)
    into customers values (50000014, 'GHA-000000044-0', 'Patricia', 'Boachie', 'Female', '14-DEC-87', 'Ghanaian', 'patricia.boachie@gmail.com', 205123469, 'Police Officer', 'Akosombo', 5, 5102002)
    into customers values (50000015, 'GHA-000000045-0', 'Robert', 'Aboagye', 'Male', '29-JAN-76', 'Ghanaian', 'robert.aboagye@gmail.com', 502123470, 'Photographer', 'Kpeve', 5, 5102003)
    into customers values (50000016, 'GHA-000000046-0', 'Nancy', 'Opoku', 'Female', '07-JUN-93', 'Ghanaian', 'nancy.opoku@gmail.com', 205123471, 'Plumber', 'Akatsi', 5, 5102001)
    into customers values (50000017, 'GHA-000000047-0', 'Jacob', 'Mawutor', 'Male', '23-JUL-81', 'Ghanaian', 'jacob.mawutor@gmail.com', 502123472, 'Politician','Asikuma', 5, 5102002)
    into customers values (50000018, 'GHA-000000048-0', 'Monica', 'Bart-plange', 'Female', '11-AUG-92', 'Ghanaian', 'monica.bart-plange@gmail.com', 205123473, 'Teacher', 'Amedzofe', 5, 5102003)
    into customers values (50000019, 'GHA-000000049-0', 'Samuel', 'Boafo', 'Male', '30-SEP-88', 'Ghanaian', 'samuel.boafo@gmail.com', 502123474, 'Data Scientist', 'Donkorkrom', 5, 5102001)
    into customers values (50000020, 'GHA-000000050-0', 'Diana', 'Bortey', 'Female', '17-OCT-90', 'Ghanaian', 'diana.bortey@gmail.com', 205123475, 'Statistician', 'Hohoe', 5, 5102002)
    into customers values (50000021, 'GHA-000000051-0', 'Daniel', 'Amevor', 'Male', '06-NOV-79', 'Ghanaian', 'daniel.amevor@gmail.com', 502123476, 'Architect', 'Akosombo', 5, 5102003)
    into customers values (50000022, 'GHA-000000052-0', 'Rebecca', 'Coblah', 'Female', '25-DEC-91', 'Ghanaian', 'rebecca.coblah@gmail.com', 205123477, 'Doctor', 'Kpeve', 5, 5102001)
    into customers values (50000023, 'GHA-000000053-0', 'Henry', 'Abankwa', 'Male', '14-FEB-85', 'Ghanaian', 'henry.abankwa@gmail.com', 502123478, 'Carpenter', 'Akatsi', 5, 5102002)
    into customers values (50000024, 'GHA-000000054-0', 'Sophia', 'Bakari', 'Female', '04-MAR-83', 'Ghanaian', 'sophia.bakari@gmail.com', 205123479, 'Nurse', 'Asikuma', 5, 5102003)
    into customers values (50000025, 'GHA-000000055-0', 'Stephen', 'Abayateye', 'Male', '20-APR-76', 'Ghanaian', 'stephen.abayateye@gmail.com', 502123480, 'Cashier', 'Amedzofe', 5, 5102001)
    into customers values (50000026, 'GHA-000000056-0', 'Alice', 'Fato', 'Female', '09-MAY-89', 'Ghanaian', 'alice.fato@gmail.com', 205123481, 'Entrepreneur', 'Donkorkrom', 5, 5102002)
    into customers values (50000027, 'GHA-000000057-0', 'Matthew', 'Ababio', 'Male', '26-JUN-87', 'Ghanaian', 'matthew.ababio@gmail.com', 502123482, 'Farmer','Hohoe', 5, 5102003)
    into customers values (50000028, 'GHA-000000058-0', 'Judith', 'Bassaw', 'Female', '16-JUL-95', 'Ghanaian', 'judith.bassaw@gmail.com', 205123483, 'Electrician','Akosombo', 5, 5102001)
    into customers values (50000029, 'GHA-000000059-0', 'George', 'Abeiku', 'Male', '04-AUG-82', 'Ghanaian', 'george.abeiku@gmail.com', 502123484, 'Fireman', 'Kpeve', 5, 5102002)
    into customers values (50000030, 'GHA-000000060-0', 'Victoria', 'Badu', 'Female', '21-SEP-86', 'Ghanaian', 'victoria.badu@gmail.com', 205123485, 'Judge','Akatsi', 5, 5102003)
select * from dual;

-- 9. ACCOUNTS TABLE 

-- EAST LEGON ACCOUNTS

insert all 
    into accounts values (01, 1000000000001, 6500.50, 'Checking', '15-FEB-12', NULL, 10000001)
    into accounts values (02, 1000000000002, 17000.75, 'Savings', '17-JUN-13', NULL, 10000002)
    into accounts values (03, 1000000000003, 18000.80, 'Checking', '12-APR-14', NULL, 10000003)
    into accounts values (04, 1000000000004, 5500.25, 'Savings', '21-JUL-15', NULL, 10000004)
    into accounts values (05, 1000000000005, 57500.90, 'Checking', '29-AUG-16', NULL, 10000005)
    into accounts values (06, 1000000000006, 9000.65, 'Savings', '19-DEC-17', NULL, 10000006)
    into accounts values (07, 1000000000007, 7200.10, 'Checking', '02-JAN-18', NULL, 10000007)
    into accounts values (08, 1000000000008, 8500.45, 'Savings', '05-MAR-19', NULL, 10000008)
    into accounts values (09, 1000000000009, 7800.20, 'Checking', '18-MAY-20', NULL, 10000009)
    into accounts values (10, 1000000000010, 8800.55, 'Savings', '23-JUL-21', NULL, 10000010)
    into accounts values (11, 1000000000011, 18300.00, 'Checking', '16-FEB-12', NULL, 10000011)
    into accounts values (12, 1000000000012, 17000.40, 'Savings', '20-JUN-13', NULL, 10000012)
    into accounts values (13, 1000000000013, 7600.50, 'Checking', '17-APR-14', NULL, 10000013)
    into accounts values (14, 1000000000014, 25400.35, 'Savings', '27-JUL-15', NULL, 10000014)
    into accounts values (15, 1000000000015, 7900.70, 'Checking', '30-AUG-16', NULL, 10000015)
    into accounts values (16, 1000000000016, 8500.55, 'Savings', '21-DEC-17', NULL, 10000016)
    into accounts values (17, 1000000000017, 47100.40, 'Checking', '06-JAN-18', NULL, 10000017)
    into accounts values (18, 1000000000018, 8200.35, 'Savings', '09-MAR-19', NULL, 10000018)
    into accounts values (19, 1000000000019, 7900.60, 'Checking', '22-MAY-20', NULL, 10000019)
    into accounts values (20, 1000000000020, 88300.50, 'Savings', '26-JUL-21', NULL, 10000020)
    into accounts values (21, 1000000000021, 7000.45, 'Checking', '19-FEB-12', NULL, 10000021)
    into accounts values (22, 1000000000022, 7500.35, 'Savings', '25-JUN-13', NULL, 10000022)
    into accounts values (23, 1000000000023, 8000.60, 'Checking', '24-APR-14', NULL, 10000023)
    into accounts values (24, 1000000000024, 15300.40, 'Savings', '31-JUL-15', NULL, 10000024)
    into accounts values (25, 1000000000025, 27800.70, 'Checking', '31-AUG-16', NULL, 10000025)
    into accounts values (26, 1000000000026, 8400.65, 'Savings', '27-DEC-17', NULL, 10000026)
    into accounts values (27, 1000000000027, 7100.55, 'Checking', '10-JAN-18', NULL, 10000027)
    into accounts values (28, 1000000000028, 8100.50, 'Savings', '15-MAR-19', NULL, 10000028)
    into accounts values (29, 1000000000029, 7800.75, 'Checking', '28-MAY-20', NULL, 10000029)
    into accounts values (30, 1000000000030, 8200.60, 'Savings', '31-JUL-21', NULL, 10000030)
select * from dual;

-- HO ACCOUNTS
insert all 
    into accounts values (31, 1000000000031, 9550.00, 'Checking', '15-APR-12', NULL, 50000001)
    into accounts values (32, 1000000000032, 10250.00, 'Savings', '16-MAY-13', NULL, 50000002)
    into accounts values (33, 1000000000033, 11150.00, 'Checking', '17-JUN-14', NULL, 50000003)
    into accounts values (34, 1000000000034, 12150.00, 'Savings', '18-JUL-15', NULL, 50000004)
    into accounts values (35, 1000000000035, 13200.00, 'Checking', '19-AUG-16', NULL, 50000005)
    into accounts values (36, 1000000000036, 14300.00, 'Savings', '20-SEP-17', NULL, 50000006)
    into accounts values (37, 1000000000037, 15500.00, 'Checking', '21-OCT-18', NULL, 50000007)
    into accounts values (38, 1000000000038, 16800.00, 'Savings', '22-NOV-19', NULL, 50000008)
    into accounts values (39, 1000000000039, 18200.00, 'Checking', '23-DEC-20', NULL, 50000009)
    into accounts values (40, 1000000000040, 19750.00, 'Savings', '24-JAN-21', NULL, 50000010)
    into accounts values (41, 1000000000041, 21400.00, 'Checking', '25-FEB-12', NULL, 50000011)
    into accounts values (42, 1000000000042, 23200.00, 'Savings', '26-MAR-13', NULL, 50000012)
    into accounts values (43, 1000000000043, 25150.00, 'Checking', '27-APR-14', NULL, 50000013)
    into accounts values (44, 1000000000044, 27250.00, 'Savings', '28-MAY-15', NULL, 50000014)
    into accounts values (45, 1000000000045, 29500.00, 'Checking', '29-JUN-16', NULL, 50000015)
    into accounts values (46, 1000000000046, 31900.00, 'Savings', '30-JUL-17', NULL, 50000016)
    into accounts values (47, 1000000000047, 34450.00, 'Checking', '31-AUG-18', NULL, 50000017)
    into accounts values (48, 1000000000048, 37150.00, 'Savings', '01-SEP-19', NULL, 50000018)
    into accounts values (49, 1000000000049, 40000.00, 'Checking', '02-OCT-20', NULL, 50000019)
    into accounts values (50, 1000000000050, 43000.00, 'Savings', '03-NOV-21', NULL, 50000020)
    into accounts values (51, 1000000000051, 46150.00, 'Checking', '04-DEC-12', NULL, 50000021)
    into accounts values (52, 1000000000052, 49450.00, 'Savings', '05-JAN-13', NULL, 50000022)
    into accounts values (53, 1000000000053, 52900.00, 'Checking', '06-FEB-14', NULL, 50000023)
    into accounts values (54, 1000000000054, 56500.00, 'Savings', '07-MAR-15', NULL, 50000024)
    into accounts values (55, 1000000000055, 60300.00, 'Checking', '08-APR-16', NULL, 50000025)
    into accounts values (56, 1000000000056, 64250.00, 'Savings', '09-MAY-17', NULL, 50000026)
    into accounts values (57, 1000000000057, 68350.00, 'Checking', '10-JUN-18', NULL, 50000027)
    into accounts values (58, 1000000000058, 72600.00, 'Savings', '11-JUL-19', NULL, 50000028)
    into accounts values (59, 1000000000059, 77000.00, 'Checking', '12-AUG-20', NULL, 50000029)
    into accounts values (60, 1000000000060, 81550.00, 'Savings', '13-SEP-21', NULL, 50000030)
select * from dual;


-- 10. CARDS TABLE

-- EAST LEGON BRANCH

insert all
    into cards values (01, 6119381277818271, 'debit', 1500.00, '16-FEB-21', '16-AUG-23', 'active', 01)
    into cards values (02, 4643258412673386, 'credit', 1000.00, '20-JUN-13', '20-JAN-16', 'expired', 02)
    into cards values (03, 1624497547593258, 'debit', 1500.00, '17-APR-22', '17-OCT-24', 'active', 03)
    into cards values (04, 9572675481992723, 'credit', 1000.00, '27-JUL-15', '27-JAN-18', 'expired', 04)
    into cards values (05, 3586942772815964, 'debit', 1500.00, '30-AUG-16', '28-FEB-19', 'expired', 05)
    into cards values (06, 7591726249265973, 'credit', 1000.00, '21-DEC-17', '21-JUN-20', 'active', 06)
    into cards values (07, 4572836758216489, 'debit', 1500.00, '06-JAN-18', '06-JUL-20', 'active', 07)
    into cards values (08, 2745678912346785, 'credit', 1000.00, '09-MAR-19', '09-SEP-21', 'active', 08)
    into cards values (09, 1872356245982745, 'debit', 1500.00, '22-MAY-20', '22-JAN-23', 'active', 09)
    into cards values (10, 4728192358471956, 'credit', 1000.00, '26-JUL-21', '26-JAN-24', 'active', 10)
    into cards values (11, 6598423781659225, 'debit', 1500.00, '19-FEB-12', '19-AUG-14', 'expired', 11)
    into cards values (12, 4893275427681932, 'credit', 1000.00, '25-JUN-13', '25-JAN-16', 'expired', 12)
    into cards values (13, 2793465982764893, 'debit', 1500.00, '24-APR-14', '24-OCT-16', 'expired', 13)
    into cards values (14, 3958274695827458, 'credit', 1000.00, '31-JUL-15', '31-JAN-18', 'expired', 14)
    into cards values (15, 7849526378495627, 'debit', 1500.00, '31-AUG-16', '28-FEB-19', 'expired', 15)
    into cards values (16, 6928374659283746, 'credit', 1000.00, '27-DEC-17', '27-JUN-20', 'active', 16)
    into cards values (17, 5637891276894231, 'debit', 1500.00, '10-JAN-18', '10-JUL-20', 'active', 17)
    into cards values (18, 2873598275498723, 'credit', 1000.00, '15-MAR-19', '15-SEP-21', 'active', 18)
    into cards values (19, 3726589274582735, 'debit', 1500.00, '28-MAY-20', '28-JAN-23', 'active', 19)
    into cards values (20, 8465938275693847, 'credit', 1000.00, '31-JUL-21', '31-JAN-24', 'active', 20)
    into cards values (21, 7592837569283756, 'debit', 1500.00, '26-JUL-21', '26-JAN-24', 'active', 21)
    into cards values (22, 7589237458923745, 'credit', 1000.00, '23-JUL-21', '23-JAN-24', 'active', 22)
    into cards values (23, 7928375692837569, 'debit', 1500.00, '22-MAY-20', '22-JAN-23', 'active', 23)
    into cards values (24, 5649832764982376, 'credit', 1000.00, '09-MAR-19', '09-SEP-21', 'active', 24)
    into cards values (25, 9275639827569384, 'debit', 1500.00, '02-JAN-18', '02-JUL-20', 'active', 25)
    into cards values (26, 7384569283465829, 'credit', 1000.00, '19-DEC-21', '19-JUN-24', 'active', 26)
    into cards values (27, 9582736598237659, 'debit', 1500.00, '29-AUG-21', '29-FEB-24', 'active', 27)
    into cards values (28, 5829375682937659, 'credit', 1000.00, '21-JUL-15', '21-JAN-18', 'expired', 28)
    into cards values (29, 4635928365982375, 'debit', 1500.00, '12-APR-14', '12-OCT-16', 'expired', 29)
    into cards values (30, 3928569283569827, 'credit', 1000.00, '17-JUN-13', '17-JAN-16', 'expired', 30)
select * from dual;

-- HO BRANCH 
INSERT ALL
    INTO cards VALUES (31, 5928364918273649, 'debit', 1500.00, '15-APR-12', '15-OCT-14', 'expired', 31)
    INTO cards VALUES (32, 4726391827392847, 'credit', 1000.00, '16-MAY-13', '16-NOV-15', 'expired', 32)
    INTO cards VALUES (33, 3948293648273946, 'debit', 1500.00, '17-JUN-14', '17-DEC-16', 'expired', 33)
    INTO cards VALUES (34, 2937465829374659, 'credit', 1000.00, '18-JUL-15', '18-JAN-18', 'expired', 34)
    INTO cards VALUES (35, 9273465827346598, 'debit', 1500.00, '19-AUG-16', '19-FEB-19', 'expired', 35)
    INTO cards VALUES (36, 4578263491827493, 'credit', 1000.00, '20-SEP-17', '20-MAR-20', 'active', 36)
    INTO cards VALUES (37, 5968273948263847, 'debit', 1500.00, '21-OCT-18', '21-APR-21', 'active', 37)
    INTO cards VALUES (38, 8273492837465938, 'credit', 1000.00, '22-NOV-19', '22-MAY-22', 'active', 38)
    INTO cards VALUES (39, 4938276482937465, 'debit', 1500.00, '23-DEC-20', '23-JUN-23', 'active', 39)
    INTO cards VALUES (40, 1827364928374659, 'credit', 1000.00, '24-JAN-21', '24-JUL-23', 'active', 40)
    INTO cards VALUES (41, 4829374659823647, 'debit', 1500.00, '25-FEB-12', '25-AUG-14', 'expired', 41)
    INTO cards VALUES (42, 7394826392746598, 'credit', 1000.00, '26-MAR-13', '26-SEP-15', 'expired', 42)
    INTO cards VALUES (43, 8273645982739465, 'debit', 1500.00, '27-APR-14', '27-OCT-16', 'expired', 43)
    INTO cards VALUES (44, 4928376495827364, 'credit', 1000.00, '28-MAY-15', '28-NOV-17', 'expired', 44)
    INTO cards VALUES (45, 3827493648293764, 'debit', 1500.00, '29-JUN-16', '29-DEC-18', 'expired', 45)
    INTO cards VALUES (46, 8293746598273469, 'credit', 1000.00, '30-JUL-17', '30-JAN-20', 'expired', 46)
    INTO cards VALUES (47, 8374659827346892, 'debit', 1500.00, '31-AUG-18', '28-FEB-21', 'active', 47)
    INTO cards VALUES (48, 4928376498273649, 'credit', 1000.00, '01-SEP-19', '01-MAR-22', 'active', 48)
    INTO cards VALUES (49, 5837264982736498, 'debit', 1500.00, '02-OCT-20', '02-APR-23', 'active', 49)
    INTO cards VALUES (50, 8376495827364982, 'credit', 1000.00, '03-NOV-21', '03-MAY-24', 'active', 50)
    INTO cards VALUES (51, 8273649827364982, 'debit', 1500.00, '04-DEC-12', '04-JUN-15', 'expired', 51)
    INTO cards VALUES (52, 4726384927364982, 'credit', 1000.00, '05-JAN-13', '05-JUL-15', 'expired', 52)
    INTO cards VALUES (53, 8374659827364983, 'debit', 1500.00, '06-FEB-14', '06-AUG-16', 'expired', 53)
    INTO cards VALUES (54, 7394827364982736, 'credit', 1000.00, '07-MAR-15', '07-SEP-17', 'expired', 54)
    INTO cards VALUES (55, 8374659827364989, 'debit', 1500.00, '08-APR-16', '08-OCT-18', 'expired', 55)
    INTO cards VALUES (56, 7346982736498273, 'credit', 1000.00, '09-MAY-17', '09-NOV-19', 'expired', 56)
    INTO cards VALUES (57, 8374659827364982, 'debit', 1500.00, '10-JUN-18', '10-DEC-20', 'active', 57)
    INTO cards VALUES (58, 7293649827364982, 'credit', 1000.00, '11-JUL-19', '11-JAN-22', 'active', 58)
    INTO cards VALUES (59, 4928374659827364, 'debit', 1500.00, '12-AUG-20', '12-FEB-23', 'active', 59)
    INTO cards VALUES (60, 7394827364982731, 'credit', 1000.00, '13-SEP-21', '13-MAR-24', 'active', 60)
SELECT * FROM dual;



-- 11. TRANSACTIONS TABLE

insert all 
    INTO transactions VALUES (01, 'deposit', '20-JAN-23', 5000.00, 0.00, 01, 1101001)
    INTO transactions VALUES (02, 'deposit', '15-FEB-23', 2500.00, 0.00, 03, 1101002)
    INTO transactions VALUES (03, 'deposit', '10-MAR-23', 7500.00, 0.00, 05, 1101003)
    INTO transactions VALUES (04, 'deposit', '05-APR-23', 3500.00, 0.00, 07, 1101001)
    INTO transactions VALUES (05, 'withdrawal', '01-FEB-23', 1000.00, 0.00, 02, 1101002)
    INTO transactions VALUES (06, 'withdrawal', '08-MAR-23', 3000.00, 0.00, 04, 1101003)
    INTO transactions VALUES (07, 'withdrawal', '13-APR-23', 4000.00, 0.00, 06, 1101001)
    INTO transactions VALUES (08, 'withdrawal', '18-MAY-23', 2000.00, 0.00, 08, 1101002)
    INTO transactions VALUES (09, 'transfer', '24-JUN-23', 6000.00, 60.00, 09, 1101003)
    INTO transactions VALUES (10, 'transfer', '30-JUL-23', 5500.00, 55.00, 10, 1101001)
    INTO transactions VALUES (11, 'deposit', '26-JAN-23', 4000.00, 0.00, 11, 1101002)
    INTO transactions VALUES (12, 'deposit', '20-FEB-23', 6000.00, 0.00, 13, 1101003)
    INTO transactions VALUES (13, 'deposit', '16-MAR-23', 4500.00, 0.00, 15, 1101001)
    INTO transactions VALUES (14, 'deposit', '12-APR-23', 3500.00, 0.00, 17, 1101002)
    INTO transactions VALUES (15, 'withdrawal', '06-FEB-23', 1500.00, 0.00, 12, 1101003)
    INTO transactions VALUES (16, 'withdrawal', '11-MAR-23', 3000.00, 0.00, 14, 1101001)
    INTO transactions VALUES (17, 'withdrawal', '17-APR-23', 5000.00, 0.00, 16, 1101002)
    INTO transactions VALUES (18, 'withdrawal', '23-MAY-23', 2000.00, 0.00, 18, 1101003)
    INTO transactions VALUES (19, 'transfer', '28-JUN-23', 7000.00, 70.00, 19, 1101001)
    INTO transactions VALUES (20, 'transfer', '25-JUL-23', 6500.00, 65.00, 20, 1101002)
select * from dual;

-- HO TRANSACTIONS

insert all 
    INTO transactions VALUES (51, 'deposit', '05-JAN-23', 2000.00, 0.00, 31, 5101001)
    INTO transactions VALUES (52, 'withdrawal', '12-JAN-23', 1500.00, 0.00, 32, 5101002)
    INTO transactions VALUES (53, 'transfer', '20-FEB-23', 2500.00, 25.00, 33, 5101003)
    INTO transactions VALUES (54, 'deposit', '14-MAR-23', 4000.00, 0.00, 34, 5101001)
    INTO transactions VALUES (55, 'withdrawal', '03-APR-23', 3500.00, 0.00, 35, 5101002)
    INTO transactions VALUES (56, 'transfer', '30-APR-23', 3000.00, 30.00, 36, 5101003)
    INTO transactions VALUES (57, 'deposit', '05-MAY-23', 1800.00, 0.00, 37, 5101001)
    INTO transactions VALUES (58, 'withdrawal', '10-JUN-23', 2000.00, 0.00, 38, 5101002)
    INTO transactions VALUES (59, 'transfer', '21-JUN-23', 2600.00, 26.00, 39, 5101003)
    INTO transactions VALUES (60, 'deposit', '08-JUL-23', 2700.00, 0.00, 40, 5101001)
    INTO transactions VALUES (61, 'withdrawal', '15-JUL-23', 3200.00, 0.00, 41, 5101002)
    INTO transactions VALUES (62, 'transfer', '25-JAN-23', 2800.00, 28.00, 42, 5101003)
    INTO transactions VALUES (63, 'deposit', '12-FEB-23', 2400.00, 0.00, 43, 5101001)
    INTO transactions VALUES (64, 'withdrawal', '02-MAR-23', 1900.00, 0.00, 44, 5101002)
    INTO transactions VALUES (65, 'transfer', '23-MAR-23', 2600.00, 26.00, 45, 5101003)
    INTO transactions VALUES (66, 'deposit', '07-APR-23', 2900.00, 0.00, 46, 5101001)
    INTO transactions VALUES (67, 'withdrawal', '15-MAY-23', 2000.00, 0.00, 47, 5101002)
    INTO transactions VALUES (68, 'deposit', '12-JUN-23', 3100.00, 0.00, 48, 5101003)
    INTO transactions VALUES (69, 'deposit', '14-JUL-23', 2200.00, 0.00, 49, 5101001)
    INTO transactions VALUES (70, 'deposit', '30-JUL-23', 2000.00, 0.00, 50, 5101002)
select * from dual;


-- 12. LOANS TABLE

-- EAST LEGON LOANS
INSERT ALL
    INTO loans VALUES (01, 85000.00, '20-FEB-22', 10000001)
    INTO loans VALUES (02, 100000.00, '15-MAR-22', 10000005)
    INTO loans VALUES (03, 70000.00, '10-APR-22', 10000009)
    INTO loans VALUES (04, 60000.00, '25-MAY-22', 10000015)
    INTO loans VALUES (05, 95000.00, '30-JUN-22', 10000020)
SELECT * FROM dual;

-- HO LOANS
INSERT ALL
    INTO loans VALUES (11, 95000.00, '01-MAR-22', 50000003)
    INTO loans VALUES (12, 80000.00, '15-APR-22', 50000010)
    INTO loans VALUES (13, 70000.00, '07-JUN-22', 50000017)
    INTO loans VALUES (14, 100000.00, '21-AUG-22', 50000025)
    INTO loans VALUES (15, 85000.00, '30-OCT-22', 50000030)
SELECT * FROM dual;

-- 13. LOAN PAYMENTS TABLE

-- EAST LEGON LOAN PAYMENTS
INSERT ALL
    INTO loans_payment VALUES (01, 2500.00, 82500.00, '01-MAR-22', 01)
    INTO loans_payment VALUES (02, 5000.00, 95000.00, '01-APR-22', 02)
    INTO loans_payment VALUES (03, 3000.00, 67000.00, '15-MAY-22', 03)
    INTO loans_payment VALUES (04, 7500.00, 52500.00, '01-JUL-22', 04)
    INTO loans_payment VALUES (05, 4000.00, 91000.00, '01-AUG-22', 05)
SELECT * FROM dual;

-- HO LOAN PAYMENTS
INSERT ALL
    INTO loans_payment VALUES (11, 2500.00, 92500.00, '01-APR-22', 11)
    INTO loans_payment VALUES (12, 5000.00, 75000.00, '16-MAY-22', 12)
    INTO loans_payment VALUES (13, 3000.00, 67000.00, '08-JUL-22', 13)
    INTO loans_payment VALUES (14, 7500.00, 92500.00, '22-SEP-22', 14)
    INTO loans_payment VALUES (15, 4000.00, 81000.00, '30-NOV-22', 15)
SELECT * FROM dual;

-- Commit changes to the database
COMMIT;

