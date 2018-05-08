import os

import pandas as pd
import sqlite3

def create_dataframe(db_filename):
    """
    Creates a dataframe by concatenating the tables in the database specified
    by db_filename, following the specific instructions in the homework.
    """
    if not os.path.exists(db_filename):
        raise ValueError(f"'{db_filename}' doesn't exist.")
    
    conn = sqlite3.connect(db_filename)	
    
    sql = """
    SELECT video_id, category_id, "ca" AS language FROM CAvideos
    UNION
    SELECT video_id, category_id, "de" AS language FROM DEvideos
    UNION
    SELECT video_id, category_id, "fr" AS language FROM FRvideos
    UNION
    SELECT video_id, category_id, "gb" AS language FROM GBvideos
    UNION
    SELECT video_id, category_id, "us" AS language FROM USvideos
    ;
    """

    return pd.read_sql_query(sql, conn)


if __name__ == '__main__':
    df = create_dataframe('../HW1-aenfield/class.db')
    print(df.shape)
