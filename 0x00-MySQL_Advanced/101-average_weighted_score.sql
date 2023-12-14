-- creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS indvd, 
        (SELECT indvd.id, SUM(score * weight) / SUM(weight) AS w_avg 
        FROM users AS indvd 
        JOIN corrections as C ON indvd.id=C.user_id 
        JOIN projects AS P ON C.project_id=P.id 
        GROUP BY indvd.id)
    AS WA
    SET indvd.average_score = WA.w_avg 
    WHERE indvd.id=WA.id;
END
$$
DELIMITER ;
