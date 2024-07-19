CREATE DATABASE IF NOT EXISTS todo_app;
USE todo_app;


CREATE TABLE members(id INT AUTO_INCREMENT PRIMARY KEY, 
                     name varchar(150), 
                     surname varchar(150), 
                     email varchar(255) NOT NULL,
                     password varchar(255) NOT NULL, 
                     profile_picture text, 
                     creation_date timestamp);
                     email_confirme BOOLEAN,




CREATE TABLE tasks(id INT AUTO_INCREMENT PRIMARY KEY,
                   title VARCHAR(255),
                   description TEXT,
                   importance INT,
                   category VARCHAR(255),
                   due_date DATE,
                   creation_date timestamp
                   done BOOLEAN NOT NULL,
                   expired BOOLEAN NOT NULL,
                   members_id INT,
                   due_time TIME, 
                   );

ALTER TABLE members ADD CONSTRAINT unique_email UNIQUE (email);
CREATE TABLE members_tasks(
                    members_id int,
                    tasks_id int
);

ALTER TABLE members_tasks ADD FOREIGN KEY(members_id) REFERENCES members(id);
ALTER TABLE members_tasks ADD FOREIGN KEY(tasks_id) REFERENCES tasks(id);