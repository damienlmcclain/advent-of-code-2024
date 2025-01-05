from typing import List


def massage_reports(reports: List[str]) -> List[List[int]]:
    """
    Given a list of strings, changes each value in the str into an int and
    returns them as a list of lists of ints.

    Parameters
    ----------
    reports
        List of str numbers separated by spaces.

    Returns
    -------
    A list of lists of ints.
    """

    massaged_reports = []
    for line in reports:
        str_numbers = line.split(' ')
        numbers = [int(x) for x in str_numbers]
        massaged_reports.append(numbers)

    return massaged_reports


def determine_safety_score(report: List[int]) -> bool:
    """
    Determines whether the report is safe by checking
    each level.

    Parameters
    ----------
    report
        List of ints to determine safety of.

    Returns
    -------
    Whether the report is safe (True) or not (False).
    """

    increasing = None
    for idx in range(len(report)):
        if idx == 0:
            continue

        previous_level = int(report[idx - 1])
        current_level = int(report[idx])

        score = current_level - previous_level
        if -3 > score or score > 3 or score == 0:
            return False
        if increasing is True and score < 0:
            return False
        if increasing is False and score > 0:
            return False

        if score < 0:
            increasing = False
        else:
            increasing = True

    return True


def tally_up_score(reports: List[str], dampener: bool = False) -> int:
    """
    Tallies up the safety score of the input reports.

    Parameters
    ----------
    reports
        List of levels as strs.
    dampener
        Whether the dampener should be enabled (True)
        or not (False).

    Returns
    -------
    The number of reports that are safe.
    """

    reports = massage_reports(reports)
    safe_reports = 0
    for report in reports:
        if determine_safety_score(report) is True:
            safe_reports += 1
        else:
            if dampener is False:
                continue
            for idx in range(len(report)):
                report_copy = report.copy()
                report_copy.pop(idx)
                if determine_safety_score(report_copy) is True:
                    safe_reports += 1
                    break

    return safe_reports
