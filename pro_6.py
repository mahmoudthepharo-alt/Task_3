def analyze_grades(grades):
    if not grades:
        return {
            "average": 0,
            "highest": None,
            "lowest": None
        }
    
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    
    return {
        "average": average,
        "highest": highest,
        "lowest": lowest
    }


grades = [85, 90, 78, 92, 88]
print(analyze_grades(grades))