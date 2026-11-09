"""
RECORD CHECK  -  my version
===========================

Name  :  Rayyan Moosa
Lane  :  AI
Date  : 09/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here

def parse_line(raw_line):
    """Clean one raw record and turn it into a dictionary."""
    parts = raw_line.strip().split(",")
    record = {"dataset": parts[0].strip()}

    for part in parts[1:]:
        if "=" in part:
            key, value = part.split("=", 1)
            key = key.strip().lower()
            value = value.strip()

            try:
                number = float(value)
                if number.is_integer():
                    value = int(number)
                else:
                    value = number
            except ValueError:
                pass

            record[key] = value

    return record


def status_of(record):
    """Flag records with an invalid rating or age."""
    rating = record.get("rating")
    age = record.get("age")

    if not isinstance(rating, (int, float)) or rating < 1 or rating > 5:
        return "FLAGGED"

    if not isinstance(age, (int, float)) or age <= 0:
        return "FLAGGED"

    return "OK"



# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = []   # replace with your code
raw_records = [
    "  Survey_2026 , rating=4 , age=23  ",
    "survey_2026, RATING = 5, AGE = 31",
    "  Customer_Feedback, rating=2, age=19 ",
    "Market_Research , RATING=6 , age=27",
    "survey_2026, rating=3, AGE = -2",
    "  Survey_2026 , Rating=high , age=24  ",
]



# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

flagged_count = 0

for raw_record in raw_records:
    pass   # replace with your code
    parsed_record = parse_line(raw_record)
    record_status = status_of(parsed_record)
    print(parsed_record, "-", record_status)

    if record_status == "FLAGGED":
        flagged_count += 1

print("Summary:", len(raw_records), "records processed,", flagged_count, "flagged.")

try:
    int("not_a_number")
except ValueError as error:
    print("Non-numeric conversion test error:", error)



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
