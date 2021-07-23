#import the relevant sql library
from sqlalchemy import create_engine
# link to your database
engine = create_engine(
    "postgres://krpwswhvgegorf:fe4909221574a8fe616626a1cbf3ae5e1beeba51d1d40f2002d635ca1f8a0763@ec2-3-233-100-43.compute-1.amazonaws.com:5432/dd261umaqv9adn",
    echo=False)
# attach the data frame (df) to the database with a name of the table; the name can be whatever you like
# df.to_sql("phil_nlp", con=engine, if_exists='append')
query = "set transaction read write; " \
        "CREATE TABLE users (PIN int PRIMARY KEY not NULL," \
        "f_name varchar(100)," \
        "l_name varchar(100)," \
        "role varchar(50)," \
        "dob date);"
"""
CREATE TABLE hours (
    PIN int not NULL,
    start_time timestamp PRIMARY KEY,
    end_time timestamp,
    hours decimal,
    duration interval,
    FOREIGN KEY (PIN) REFERENCES users(PIN)
    );
INSERT INTO users VALUES (100, 'Levon', 'Yeghiazaryan', 'administrator', '08.11.1990'), (101, 'Lida', 'Muradyan', 'lawyer', '10.04.1998');
SELECT * FROM users;"
"""
print(engine.execute(query).fetchone())
# run a quick test
print(engine.execute("SELECT * FROM phil_nlp").fetchone())
