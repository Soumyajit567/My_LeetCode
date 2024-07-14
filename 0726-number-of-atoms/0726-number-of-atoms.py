class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [{}]
        i, n = 0, len(formula)
        
        while i < n:
            if formula[i] == '(':
                # Start a new scope
                stack.append({})
                i += 1
            elif formula[i] == ')':
                # End of current scope, get the multiplier
                i += 1
                j = i
                while j < n and formula[j].isdigit():
                    j += 1
                multiplier = int(formula[i:j]) if i != j else 1
                i = j
                # Pop the top scope and multiply all counts by the multiplier
                top = stack.pop()
                for element, count in top.items():
                    stack[-1][element] = stack[-1].get(element, 0) + count * multiplier
            else:
                # Read the element name
                j = i + 1
                while j < n and formula[j].islower():
                    j += 1
                element = formula[i:j]
                i = j
                # Read the count
                j = i
                while j < n and formula[j].isdigit():
                    j += 1
                count = int(formula[i:j]) if i != j else 1
                i = j
                # Update the current scope
                stack[-1][element] = stack[-1].get(element, 0) + count

        # Now we have a single dictionary at the end of processing
        result = []
        for element in sorted(stack[0].keys()):
            count = stack[0][element]
            result.append(f"{element}{count if count > 1 else ''}")
        return "".join(result)
            