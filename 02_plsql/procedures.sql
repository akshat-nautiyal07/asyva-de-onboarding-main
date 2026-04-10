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