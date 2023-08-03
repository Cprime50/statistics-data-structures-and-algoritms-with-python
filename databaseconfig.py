import psycopg2

from main import (
    find_mean_colour,
    find_mode_colour,
    find_median_colour,
    find_variance_colour,
    find_probability_red,
    data
)


def save_db(data, connection_string):
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS colour_statistics (
        day VARCHAR(20),
        mean FLOAT,
        mode VARCHAR(20),
        median VARCHAR(20),
        variance FLOAT,
        probability_red FLOAT
    );
    """
    cursor.execute(create_table_query)
    connection.commit()

    for day, colours_str in data.items():
        mean = find_mean_colour(colours_str)
        mode = find_mode_colour(colours_str)
        median = find_median_colour(colours_str)
        variance = find_variance_colour(colours_str)
        probability_red = find_probability_red(colours_str)

        sql = "INSERT INTO colour_statistics (day, mean, mode, median, variance, probability_red) VALUES (%s, %s, %s, %s, %s, %s);"
        cursor.execute(sql, (day, mean, mode, median, variance, probability_red))

    connection.commit()
    connection.close()


connection_string = "postgres://charles:4vvpa3XzEXXsGFUOafqw3MEH8dPsUUP4@dpg-cj5s4k2cn0vc73fvka5g-a.oregon-postgres.render.com/colours"
save_db(data, connection_string)
