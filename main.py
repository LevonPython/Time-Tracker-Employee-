from panels import main_win, admin_win, emp_win
import re, os, psycopg2

if __name__ == "__main__":
    m = main_win()
    m.main.run()
    # cnx = psycopg2.connect("postgres://krpwswhvgegorf:fe4909221574a8fe616626a1cbf3ae5e1beeba51d1d40f2002d635ca1f8a0763@ec2-3-233-100-43.compute-1.amazonaws.com:5432/dd261umaqv9adn", sslmode='require')
    # cursor = cnx.cursor()
    # print(f'cursor: at {cursor}')
    # adm = emp_win(cnx, cursor, 255, "Levon", "Yeghiazaryan")
