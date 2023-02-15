import psycopg2


def execute_query(query, params=None, fetch=True):
    """
    -> a function to execute PostgreSQL queries
    :param query: sql query with placeholders (%s) in place of variables
    :param params: parameters in order and inside a TUPLE
    :param fetch: set to True if query awaits some return value. False otherwise.
    :return: list of dictionary with items.
    """
    # Replace the values in angle brackets with your own PostgreSQL database credentials
    conn = psycopg2.connect(
        host='<YOUR_HOST>',
        database='<YOUR_DATABASE>',
        user='<YOUR_USERNAME>',
        password='<YOUR_PASSWORD>'
    )

    with conn:
        with conn.cursor() as cursor:
            if params is None:
                cursor.execute(query)
            else:
                cursor.execute(query, params)

            if fetch:
                columns = [col.name for col in cursor.description]
                result = [dict(zip(columns, row)) for row in cursor.fetchall()]
                return result

            else:
                conn.commit()
