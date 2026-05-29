def generate_suggestions(features):

    suggestions = []

    loc = features.get("loc", 0)
    complexity = features.get("avg_complexity", 0)
    maintainability = features.get("maintainability", 100)
    imports = features.get("import_count", 0)
    functions = features.get("function_count", 0)

    # Rule 1: High complexity
    if complexity > 10:
        suggestions.append("Reduce code complexity by breaking nested loops or conditions.")

    # Rule 2: Large code
    if loc > 150:
        suggestions.append("Function is too long. Break it into smaller reusable functions.")

    # Rule 3: Low maintainability
    if maintainability < 60:
        suggestions.append("Improve readability by adding comments and simplifying logic.")

    # Rule 4: Too many imports
    if imports > 10:
        suggestions.append("Remove unused imports to clean up the code.")

    # Rule 5: Few functions
    if functions < 2:
        suggestions.append("Split code into multiple functions for better modularity.")

    if not suggestions:
        suggestions.append("Code structure looks clean. Good job!")

    return suggestions