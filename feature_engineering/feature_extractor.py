import ast

from radon.raw import analyze
from radon.metrics import mi_visit
from radon.complexity import cc_visit


def extract_features(code):

    features = {}

    try:

        
        # Raw Metrics
        
        raw = analyze(code)

        features["loc"] = raw.loc
        features["lloc"] = raw.lloc
        features["sloc"] = raw.sloc
        features["comments"] = raw.comments

        
        # Maintainability Index
        
        features["maintainability"] = mi_visit(
            code,
            multi=True
        )

        
        # Cyclomatic Complexity
        
        complexity = cc_visit(code)

        if complexity:

            avg_complexity = sum(
                c.complexity for c in complexity
            ) / len(complexity)

        else:
            avg_complexity = 0

        features["avg_complexity"] = avg_complexity

        
        # AST Features
        
        tree = ast.parse(code)

        function_count = len([
            node for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef)
        ])

        class_count = len([
            node for node in ast.walk(tree)
            if isinstance(node, ast.ClassDef)
        ])

        import_count = len([
            node for node in ast.walk(tree)
            if isinstance(node, ast.Import)
        ])

        features["function_count"] = function_count
        features["class_count"] = class_count
        features["import_count"] = import_count

    except Exception as e:

        print("Error processing code:")
        print(e)

        return None

    return features