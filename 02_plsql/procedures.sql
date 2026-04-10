-- Write your procedure(s) here

DECLARE
v_message VARCHAR2(100);
v_count NUMBER;
BEGIN
v_message := 'Hello, Everyone'
SELECT COUNT(*) INTO v_count FROM EMPLOYEES;
DBMS_OUTPUT.PUT_LINE("Total count: " || v_count);
EXCEPTION
WHEN OTHERS THEN
DBMS_OUTPUT.PUT_LINE('error' || SQLERRM)
END:


-- ##IF-ELSE STATEMENT

DECLARE
v_marks NUMBER := 78;
v_grade VARCHAR2(5);
BEGIN
IF v_marks >= 90 THEN
v_grade := 'A';
ELSIF v_marks >=70 THEN
v_grade := 'B';
ELSIF v_marks >= 50 THEN
v_grade := 'C';
ELSE
v_grade := 'D';
END IF;
DBMS_OUTPUT.PUT_LINE('grade: ' || v_grade);
END;


-- ## SWITCH CASE

DECLARE
v_status VARCHAR2(20) := 'LOADING';
v_action VARCHAR2(20);
BEGIN
v_action := CASE v_status
WHEN 'PENDING' THEN 'SHIFT TO LOADING'
WHEN 'LOADING' THEN 'SHIFT TO RUNNING'
WHEN 'RUNNING' THEN 'WAIT'
ELSE 'RETRY'
END;
DBMS_OUTPUT.PUT_LINE(v_action);
END;


-- ## LOOP WITH EXIT WHEN

DECLARE
v_i PLS_INTEGER;
v_sum NUMBER := 0;
BEGIN
v_i := 1;
LOOP
v_sum := v_sum + v_i;
EXIT WHEN v_i >=5;
v_i := v_i + 1;
END LOOP;
DBMS_OUTPUT.PUT_LINE(v_sum);
END;


-- ## WHILE LOOP
DECLARE
v_i PLS_INTEGER;
v_sum NUMBER := 0;
BEGIN
v_i := 1;
WHILE v_i <= 5 LOOP
v_sum := v_sum + v_i;
v_i := v_i + 1;
END LOOP;
DBMS_OUTPUT.PUT_LINE(v_sum);
END;


-- ## FOR LOOP
BEGIN
FOR i IN 1..6 LOOP
DBMS_OUTPUT.PUT_LINE('Current value of i is: ' || i);
END LOOP;
END;




CREATE TABLE Employees (
  e_id     NUMBER PRIMARY KEY,
  e_name   VARCHAR2(50),
  salary   NUMBER,
  dept     VARCHAR2(30)
);

INSERT INTO Employees VALUES (1, 'Akshat', 3000, 'IT');
INSERT INTO Employees VALUES (2, 'Kumar', 4500, 'HR');
INSERT INTO Employees VALUES (3, 'Nautiyal', 5000, 'IT');
INSERT INTO Employees VALUES (4, 'John', 2500, 'Finance');
INSERT INTO Employees VALUES (5, 'Emma', 6000, 'IT');


DECLARE
  CURSOR emp_cursor is
    SELECT  e_name from Employees;
  v_name Employees.e_name%TYPE;
BEGIN
    OPEN emp_cursor;
    LOOP
    FETCH emp_cursor INTO v_name;
    EXIT WHEN emp_cursor%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(v_name);
    END LOOP;
    CLOSE emp_cursor;
END;