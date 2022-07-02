-- Creates a stored procedure AddBons that adds a new correction for a student.
-- Parameters:
--	user_id, a user.id value.
-- 	project_name, a new or already exist project - if no project.name
--	    found in table, creates it.
--	score, the score value of the correction.

DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	DECLARE proj_id INT;
	IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0
	THEN
		INSERT INTO projects (name) VALUES (project_name);
	END IF;
	SET proj_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
	INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, proj_id, score);
END
//

DELIMITER ;

