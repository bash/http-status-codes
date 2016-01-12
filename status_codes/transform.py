#
# (c) 2016 Ruben Schmidmeister
#

import csv
import io


def transform(data):
    reader = csv.DictReader(io.StringIO(data), fieldnames=['Value', 'Description', 'Reference'], dialect='unix')
    document = {}

    # skip headers
    next(reader)

    for row in reader:
        description = row['Description']

        # ignore unassigned codes
        if description == 'Unassigned':
            continue

        if description == '(Unused)':
            continue

        code = int(row['Value'])
        document[code] = description

    return document
