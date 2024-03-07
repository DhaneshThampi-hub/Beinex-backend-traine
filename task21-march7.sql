use beinex;
CREATE TABLE PersonInfo (
    PersonID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    Gender VARCHAR(10),
    City VARCHAR(50),
    Salary DECIMAL(10, 2),
    Email VARCHAR(100),
    EducationLevel VARCHAR(20),
    PhoneNumber bigint(15)
);

INSERT INTO PersonInfo VALUES
(1, 'John', 'Doe', 25, 'Male', 'New York', 60000.50, 'john.doe@email.com', 'Bachelor', 55512398764),
(2, 'Jane', 'Smith', 30, 'Female', 'Los Angeles', 75000.75, 'jane.smith@email.com', 'Master', 5555678),
(3, 'Bob', 'Johnson', 22, 'Male', 'Chicago', 50000.25, 'bob.johnson@email.com', 'High School', 5558989876),
(4,'Abhinav','KP',26,'Male','Kochi',21000.34,'abinavkp@gamail.com','Btech',585995849),
(5,'Bincy','Biju',24,'Female','Kochi',30000,'bincybiju@gamil.com','MCA',5809949283),
(6,'Parvathy','Krishna',23,'Female','Kottaym',30000.34,'parvvathy@gmail.com','Btech',9576847544),
(7,'Sonu','Yohannan',24,'Male','Pthananmthitta',49000,'sonu@gamiil.com','MCA',39586768695),
(8,'Blair','Tony',28,'Male','Thrisuur',500000,'blair@gmail.com','Btech',78575905958),
(9,'Blair','T',23,'Male','Thrisuur',50000,'blairt@gmail.com','Btech',78475905968),
(10, 'Alice', 'Williams', 28, 'Female', 'Miami', 70000.00, 'alice.williams@email.com', 'Bachelor', 5554321977);



-- Scenario 1 - Select all columns for  people aged 25 or older:
SELECT * FROM PersonInfo WHERE Age >= 25;


-- Scenario 2 - Select distinct cities from the table:
SELECT DISTINCT City FROM PersonInfo;

-- Scenario 3 - Select first and last names for females with a Master's degree:
SELECT FirstName, LastName FROM PersonInfo WHERE Gender = 'Female' AND EducationLevel = 'Btech';


-- Scenario 4 - Select individuals earning between $50,000 and $60,000:
SELECT * FROM PersonInfo WHERE Salary BETWEEN 50000 AND 60000;

-- Scenario 5 - Select records for people in New York or Los Angeles:
SELECT * FROM PersonInfo WHERE City IN ('New York', 'Los Angeles');


-- Scenario 6 - Select people with either a Bachelor's or Master's degree:
SELECT * FROM PersonInfo WHERE EducationLevel IN ('Bachelor', 'Master');

-- Scenario 7 - Select people aged 30 or younger with a salary greater than $70,000:
SELECT * FROM PersonInfo WHERE Age <= 30 AND Salary > 70000;

-- Scenario 8 - Select people with an email ending in "@email.com":
SELECT * FROM PersonInfo WHERE Email LIKE '%@email.com';


-- Scenario 9 - Select people from Kochi or Kottayam who are not in their 20s:
SELECT * FROM PersonInfo WHERE (City = 'Kochi' OR City = 'Kottaym') AND  Age BETWEEN 20 AND 29;

-- Scenario 10 - Select people with a salary less than $60000 and who are either from kochi or have a Bachelor's degree:
SELECT * FROM PersonInfo WHERE Salary < 60000 AND (City = 'Kochi' OR EducationLevel = 'Bachelor');

-- Scenario 11 - Select people with a phone number starting with '555':
SELECT * FROM PersonInfo WHERE PhoneNumber LIKE '555%';

-- Scenario 12 - Select people who are either under 25 or over 35:
SELECT * FROM PersonInfo WHERE Age < 25 OR Age > 35;

-- Scenario 13 - Select people with a salary greater than $50000 and who are not from New York:
SELECT * FROM PersonInfo WHERE Salary > 50000 AND NOT City = 'New York';

-- Scenario 14 - Select people with a salary greater than $70000 or who have a Master's degree:
SELECT * FROM PersonInfo WHERE Salary > 70000 OR EducationLevel = 'Master';

-- Scenario 15 - Select people aged 25-30 who are either from Chicago or have a Bachelor's degree:
SELECT * FROM PersonInfo WHERE (Age BETWEEN 25 AND 30) AND (City = 'Chicago' OR EducationLevel = 'Bachelor');

