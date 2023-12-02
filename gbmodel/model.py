class Model():
    def select(self):
        """
        Gets all rows from the database as a list of lists.
        Row consists of text body and timestamp
        :return: List of lists containing all rows of database
        """
        pass

    def insert(self, body, timestamp, sentiment):
        """
        Inserts entry into database
        :param body: String
        :param timestamp: datetime
        :raises: Database errors on connection and insertion
        """
        pass
