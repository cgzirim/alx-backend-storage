-- Creates a stored procedure ComputeAverageScoreForUser that computes and
-- store the average score for a student.
-- Parameter:
--	user_id, a user.id value

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE average FLOAT;

	SET average = (SELECT AVG(score) FROM corrections WHERE user_id = user_id);

	UPDATE users SET users.average_score = average WHERE id = user_id;
END
//

DELIMITER ;
