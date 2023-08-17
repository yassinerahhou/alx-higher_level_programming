-- count
select score ,
count(*) as number fromFROM second_table GROUP BY score ORDER BY score DESC ;
