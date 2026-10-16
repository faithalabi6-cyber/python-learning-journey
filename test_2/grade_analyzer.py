def analyze_grade(scores):
    for score in scores:
        if score < 50:
            print("Found a failing grade")
        else:
            continue

analyze_grade([85, 42, 90, 35])
