-- Creates a function called SafeDiv that divides (and returns) the
-- first by the second number or returns 0 if the second number is equal to 0.
-- Arguments:
--	a, INT
--	b, INT
-- Returns a / b or 0 if b == 0

DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER //

CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	IF b = 0 THEN RETURN 0;
	END IF;

	RETURN a / b;
END;
//

DELIMITER ;
