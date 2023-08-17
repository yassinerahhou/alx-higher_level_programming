-- count
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER by number DESC, score;
