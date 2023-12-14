-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- computes and store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    user_id INTEGER
)
BEGIN
    DECLARE w_average_score FLOAT;
    SET w_average_score = (SELECT SUM(score * weight) / SUM(weight) 
                        FROM users AS U 
                        JOIN corrections as C ON U.id=C.user_id 
                        JOIN projects AS P ON C.project_id=P.id 
                        WHERE U.id=user_id);
    UPDATE users SET average_score = w_average_score WHERE id=user_id;
END
$$
DELIMITER ;
