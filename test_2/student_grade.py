lis = [1,2,3,4,5,6,7]

newlis = map(lambda x: x**2, lis )

newlis1 = list(filter(lambda x: x%2==0 , lis ))
print(newlis1)




students = [
    {"name": "Sam", "scores": [80, 90]},
    {"name": "David", "scores": [55, 60]}
]


# Grading System
# 70–100 → A
# 60–69 → B
# 50–59 → C
# 45–49 → D
# 40–44 → E
# 0–39 → F
def calculate_average(scores: list[int]) -> float:
    total = 0
    for score in scores:
        total += score
    return round(total/len(scores), 2)

def get_student_info(student: dict[str: str, str:list[int]]) -> tuple[str, float, str]:
    name = student['name']
    avg_score = calculate_average(student['scores'])
    grade = grade_for(avg_score)

    return name, avg_score, grade


def grade_for(avg: float) -> str:
    if avg <= 39:
        grade = "F"
    elif avg <= 44:
        grade = "E"
    elif avg <= 49:
        grade = "D"
    elif avg <= 59:
        grade = "C"
    elif avg <= 69:
        grade = "B"
    else:
        grade = "A"

    return grade

