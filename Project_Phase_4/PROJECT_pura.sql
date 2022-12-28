-- db_try
CREATE TABLE department
(
    dept_name       varchar(50) not null,
    head_of_dept    varchar(20) not null,
    building_no     int,
    PRIMARY KEY     (dept_name)
);

CREATE TABLE hostel
(
    hostel_name         varchar(20) not null,
    no_of_students      int         not null,
    capacity            int         not null,
    gender              varchar(10),
    warden              varchar(30),
    capacity_per_room   int         not null,
    PRIMARY KEY         (hostel_name)
);

CREATE TABLE students
(
    roll_no     int         not null,
    cgpa        int(10),
    gender      char(1),
    batch       varchar(10) not null,
    age         int,
    dept        varchar(20) not null,
    email       varchar(50) not null,
    dob         date,
    st_name     varchar(50) not null,
    st_password varchar(20) not null,
    hostel_name varchar(20),
    PRIMARY KEY (roll_no),  
    FOREIGN KEY (dept)          references  department(dept_name), 
    FOREIGN KEY (hostel_name)   references  hostel(hostel_name)
);

CREATE TABLE sports
(
    sport_name      varchar(20) not null,
    in_charge_name  varchar(20),
    equipment       varchar(20),
    ground          varchar(20),
    hostel_won      varchar(20),
    PRIMARY KEY     (sport_name),
    FOREIGN KEY     (hostel_won)    references hostel(hostel_name)
);


-- done

CREATE TABLE equipment
(
    equip_name      varchar(20)  not null,  
    -- isko int karo
    quantity        int,
    size            int,
    sport_name      varchar(20)  not null,
    PRIMARY KEY     (equip_name),
    FOREIGN KEY     (sport_name) references sports(sport_name)
);

CREATE TABLE mess
(
    mess_name       varchar(20)     not null,
    hostel_name     varchar(20)     not null,
    students_reg    int             not null,
    PRIMARY KEY     (mess_name),
    FOREIGN KEY     (hostel_name)   references hostel(hostel_name)
);

-- done
CREATE TABLE locations
(
    place_name  varchar(20) not null,
    street      varchar(20) not null,
    capacity    int,
    PRIMARY KEY (place_name)
);

-- done
CREATE TABLE subjects
(
    course_id       int not null,
    lab             char(1),
    no_of_students  int not null,
    prof_id         int,
    subject_name    varchar(20),
    PRIMARY KEY (course_id)
);

-- done
CREATE TABLE clubs
(
    club_name       varchar(30) not null,
    no_of_members   int         not null,
    coord1          varchar(20),
    coord2          varchar(20),
    coord3          varchar(20),
    PRIMARY KEY     (club_name)
);

-- done
CREATE TABLE professors
(
    prof_id         int         not null,
    prof_name       varchar(30) not null,
    gender          char(1)     not null,
    dept            varchar(20),
    salary          int,
    course_id       int,
    dob             date      not null,
    age             int,
    super_prof_id   int,
    PRIMARY KEY     (prof_id),
    FOREIGN KEY     (super_prof_id) references  professors(prof_id)
);

-- CREATE TABLE belongs_to
-- (
--     prof_id     int not null,
--     dept_name   varchar(50) not null,
--     FOREIGN KEY (dept_name) references  department(dept_name),
--     FOREIGN KEY (prof_id)   references  professors(prof_id)
-- );

CREATE TABLE member_of
(
    std_roll_no int         not null,
    club_name   varchar(30) not null,
    FOREIGN KEY (std_roll_no)   references  students(roll_no),
    FOREIGN KEY (club_name)     references  clubs(club_name)
);

CREATE TABLE teaches_at
(
    course_id   int not null,
    prof_id     int not null,
    building    varchar(20) not null,
    std_roll_no int not null,
    FOREIGN KEY (building) references locations(place_name),
    FOREIGN KEY (prof_id)  references professors(prof_id),
    FOREIGN KEY (course_id)   references  subjects(course_id),
    FOREIGN KEY (std_roll_no) references  students(roll_no)
);

CREATE TABLE subject_prof_id
(
    course_id   int not null,
    prof_id     int not null,
    FOREIGN KEY (course_id) references subjects(course_id),
    FOREIGN KEY (prof_id)   references professors(prof_id)
);

-- CREATE TABLE competes_with
-- (
--     hostel1 varchar(20) not null,
--     hostel2 varchar(20) not null,
--     FOREIGN KEY hostel1 references hostel(hostel_name),
--     FOREIGN KEY hostel2 references hostel(hostel_name)
-- );

insert into professors values 
(1,'Sunil','M','cse',20000,8, '1980-7-12',42,NULL),
(2,'Yashaswi','F','iot',200000,1 , '1970-8-1',52,1),
(3,'Siddhi','F','ece',450000, 4, '1965-9-30',57,NULL),
(4,'jwel','M','mathematics',170000, 9, '1985-10-7',37,3),
(5,'vedant','M','linguistics',77000, 10, '1985-1-7',37,1),
(6,'Tejas Bodas','M','mathematics',77000, 2, '1984-1-7',38,1),
(7,'Suresh Purini','M','cse',77000, 3, '1965-1-7',57,1),
(8,'Aftab Hussain','M','iot',77000, 5, '1963-1-7',59,1),
(9,'Radhika Mamidi','F','linguistics',77000, 1, '1985-1-7',37,1),
(10,'Sachin Chaudhari','M','ece',77000, 7, '1985-1-7',37,1);

insert into department values
('mathematics','Tejas Bodas',3),
('cse','Suresh Purini',1),
('iot','Aftab Hussain',2),
('linguistics','Radhika Mamidi',4),
('humanities','Yashaswi',5),
('ece','Sachin Chaudhari',2);

insert into hostel values
('parijat',250, 300,'F','Kavita',2),
('bakul',500, 500,'M','Bhanupratap',2),
('palash',400, 600,'M','Nadeem',1),
('kadamb',50, 100,'M','Raju',1),
('gheb',200, 200,'F','Kavita',1);

insert into students values 
(1,NULL,'F','ug2k21',18,'mathematics','1@email.com','2003-11-28','Shambhavi','password','parijat'),
(2,NULL,'M','ug2k21',19,'cse','2@email.com','2002-08-16','Vansh','passy','bakul'),
(3,NULL,'M','ug2k21',18,'iot','3@email.com','2004-03-27','Yatharth','pasu','bakul'),
(4,NULL,'F','ug2k21',10,'linguistics','4@email.com','2008-01-02','Ananya','vaibhu','parijat'),
(5,NULL,'M','ug2k21',15,'humanities','5@yahoo.com','2006-08-16','Arya','ananya','bakul'),
(6,NULL,'M','ug2k21',10,'cse','6@email.com','2008-01-02','Rayaan','vaibhu','parijat'),
(7,NULL,'M','ug2k21',18,'ece','7@email.com','2008-01-02','Yash','vaibhu','parijat'),
(8,NULL,'F','ug2k21',19,'linguistics','8@email.com','2008-01-02','Shruti','vaibhu','parijat'),
(9,NULL,'M','ug2k21',19,'humanities','9@email.com','2008-01-02','Akhil','vaibhu','parijat'),
(10,NULL,'F','ug2k21',18,'iot','10@email.com','2008-01-02','Santhu','vaibhu','parijat');

-- subjects used in : teaches_at, subject_prof_id
insert into subjects values 
(101 , 'n', 89,1,'algorithm analysis'),
(102 , 'y', 120,7,'computer programming'),
(301 , 'y', 17,3,'biology'),
(201 , 'y', 50,8,'embedded systems'),
(202 , 'y' ,100,10,'microcontrollers'),
(401 , 'n' ,100,9,'nlp'),
(501 , 'n' ,100,6,'probability'),
(302 , 'n' ,100,2,'human studies'),
(203 , 'n' ,100,4,'communications');

insert into clubs values
('tdc',22,'Shambhavi','Ananya',NULL),
('artsoc',10,'Yatharth','Arya','Vansh'),
('ecell',1,'Vansh',NULL,NULL),
('decore',2,'Ananya',NULL,NULL),
('erc',50,'Arya','Vansh','Ananya');

insert into sports values
('badminton','Shambhavi',NULL,'NBH',NULL),
('cricket','Ananya',NULL,'FG',NULL),
('tabletennis','Yatharth',NULL,'Warehouse',NULL),
('football','Vansh',NULL,NULL,null),
('swimming','Arya',NULL,'Gachibowli Stadium',NULL);

insert into mess values
('yukthahar', 'bakul' , 100),
('kadam', 'parijat' , 150),
('south', 'bakul' , 75),
('north', 'parijat' , 200);

insert into locations values
('Himalaya','research street',750),
('Vindhya','research street', 1000),
('Football Ground','kadamb road',1000),
('T-Hub','research street',NULL),
('Kadamb Mess','kadamb road',150);

insert into equipment values
('TT-rackets', 10, NULL, 'TableTennis'),
('Footballs', 4, NULL, 'Football'),
('Badminton Rackets', 20, NULL, 'Badminton'),
('Cricket Bats', 10, NULL, 'Cricket'),
('Cricket Balls', 15, NULL, 'Cricket');

-- insert into competes_with values
-- ('parijat', 'gheb'),
-- ('palash','bakul');

insert into member_of values
(1,'tdc'),
(2,'artsoc'),
(3,'artsoc'),
(4,'erc'),
(5,'erc'),
(4,'decore');

insert into subject_prof_id values
(101,7),
(102,1),
(201,10),
(202,3),
(203,10),
(301,9),
(302,2),
(501,6),
(401,1);

insert into teaches_at values
(101,7,"Himalaya",1),
(101,7,"Himalaya",2),
(101,7,"Vindhya",3),
(101,7,"Football Ground",10),
(101,7,"Himalaya",6),
(102,1,"T-Hub",1),
(102,1,"Football Ground",2),
(102,1,"Himalaya",3),
(102,1,"Vindhya",6),
(102,1,"T-Hub",7),
(102,1,"Vindhya",10),
(201,10,"Himalaya",3),
(201,10,"T-Hub",7),
(201,10,"Vindhya",10),
(301,9,"Kadamb Mess",5),
(301,9,"Himalaya",9),
(302,2,"Football Ground",5),
(302,2,"Vindhya",9),
(501,6,"T-Hub",1),
(501,6,"Himalaya",2),
(501,6,"Kadamb Mess",3),
(501,6,"Vindhya",4),
(501,6,"T-Hub",5),
(501,6,"Vindhya",6),
(501,6,"Football Ground",7),
(501,6,"Himalaya",8),
(501,6,"T-Hub",9),
(501,6,"Himalaya",10),
(401,1,"Himalaya",4),
(401,1,"Himalaya",8);
