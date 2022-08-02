from sqlalchemy import create_engine, text


def create_eng():
    engine = create_engine("sqlite:///some.db", future=True)
    return engine

def connect_eng():
    """
    Connect to a database
    """
    engine = create_eng()
    connection = engine.connect()
    # print(engine)
    # print(connection)
    # print(connection.connection)
    # print(connection.connection.connection)
    return connection

def execute():
    with connect_eng() as conn:
        stmt = text("select 'hello world'")
        # stmt_2 = text("select emp_id, emp_name from employee where emp_id=:emp_id")
        result = conn.execute(stmt)
        print(type(result))
        print( result.all() )
        print(type(result.all()))

def create_table_insert_data():
    with connect_eng() as conn:
        # conn.execute(text("CREATE TABLE another_table (x str, y str)"))
        conn.execute(
            text("INSERT INTO another_table (x, y) VALUES (:x, :y)"),
            [{"x": "henlo", "y":1}, {"x":"world", "y":4 }]
        )
        conn.commit()

def fetching_rows():
    with connect_eng() as conn:
        result = conn.execute(text("SELECT x, y FROM another_table"))
        for row in result:
            print(f"x: {row.x} y: {row.y}")

def fetching_with_params():
    with connect_eng() as conn:
        result = conn.execute(
            text("SELECT x, y FROM another_table WHERE y > :y"),
            {"y": 2}
        )
        for row in result:
            print(f"x: {row.x} y:{row.y}")

def bundle_params_and_statement(param):
    statement = text("SELECT x, y FROM another_table WHERE y >= :y ORDER BY x, y").bindparams(y=param)
    with connect_eng() as conn:
        result = conn.execute(statement)
        for row in result:
            print(f"x: {row.x} y: {row.y}")
