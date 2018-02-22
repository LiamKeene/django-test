from django.db import models

"""Create a `Plan` class with two choices fields, option_1 and option_2.

"""


"""Create queries for the Enrolment model that will allow us to query Enrolments
that are 'not_synced', ie completed but not exported.

"""



class Enrolment(models.Model):
    field_of_interest = models.CharField(max_length=255)

    completed = models.DateTimeField(null=True)
    exported = models.DateTimeField(null=True)

    """Write a function to return a query string required for an integration.

    Normally we would use a service, if you have time feel free to write one :)

    We need to replace the `<list of formatted IDs>` with the IDs of Enrolments that
    are not synced but we need to format them so that they are a string;

    Enrol-<id>, etc

    Each formatted ID needs to be quoted with single quotes, they must be comma separated
    and the whole list must be enclosed in parentheses.

    for example ('Enrol-1', 'Enrol-2')

    """
    def query_string(self):
        return """
            SELECT
                table.someId, table.fieldToSync, table.firstField, table.secondField
            FROM
                table
            WHERE
                table.someId IN <list of formatted IDs>
            """
