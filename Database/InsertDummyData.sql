USE `recurDB`;

INSERT INTO
	`UserType` (userType)
VALUES
	('user')
    ,('admin');

INSERT INTO
	`User` (userTypeID_FK,username,password,firstName,lastName,email,phone)
VALUES
	(1,'welkin','candela','Morgan','Mitchell','mlevimitchell@gmail.com','+61432712472')
    ,(1,'yodaquette','rocket','Andrew','Goodman','a.goodmanr@gmail.com','4782837050')
    ,(2,'welkin_warrior','candela2','','','','');