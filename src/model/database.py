import sqlite3


class Database:
    
    def __init__(self) -> None:
        self.connection = sqlite3.connect("database.sqlite3")
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, *attrs):
        """
            use this function to create a database table.

            Args:
                table_name ([str]): [table name]
                attrs ([str]): [attributes of table]
        """

        try:
            print("Creating table...")
            self.cursor.execute(
                f"""
                    CREATE TABLE {table_name} ({attrs})
                """
            )
            self.connection.commit()
            print("Table created!!!")
        except Exception as error:
            print(error)
        finally:
            self.connection.close()

    def drop_table(self, table_name):
        """
            Use this function to drop a table

        Args:
            table_name ([str]): [table name]
        """

        try:
            print(f'Droping table {table_name}')
            self.cursor.execute(
                f"""
                    DROP TABLE {table_name}
                """
            )
            self.connection.commit()
            print(f'Table {table_name} dropped!')
        except Exception as error:
            print(error)
        finally:
            self.connection.close()

    def truncate_table(self, table_name):
        """
            Use this to truncate selected table

        Args:
            table_name ([str]): [table name]
        """

        try:
            print(f'clearing table {table_name}')
            self.cursor.execute(
                f"""
                    DELETE TABLE {table_name}
                """
            )
            self.connection.commit()
            print(f'Table {table_name} was cleaned!')
        except Exception as error:
            print(error)
        finally:
            self.connection.close()