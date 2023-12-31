#!/usr/bin/env python3

from csv import DictReader
import json
import fileinput


def to_json(input):
    reader = DictReader(input, dialect="unix")
    assigned_entries = [entry for entry in reader if is_assigned(entry)]
    status_codes = {
        int(entry["Value"]): entry["Description"] for entry in assigned_entries
    }
    return json.dumps(status_codes, indent=4, sort_keys=True)


def is_assigned(entry):
    return entry["Description"] not in ["Unassigned", "(Unused)"]


if __name__ == "__main__":
    print(to_json(fileinput.input()))
