# AI Coding Agent Instructions - Loop Tasks Project

## Project Overview
This is an **intern training project** demonstrating Python loop constructs, control flow, and practical use cases. The project is educational in nature with 8 progressively complex examples.

## Key Project Characteristics

### Purpose
- Teach fundamental Python looping concepts: `for`, `while`, `break`, `continue`
- Demonstrate real-world applications (counters, tables, cart totals)
- Show iteration patterns with strings, ranges, and lists

### Code Organization Pattern
Each demonstration is organized with:
1. Clear section headers (`# --------------------------------------------------`)
2. Brief description (number and topic)
3. Working code example with `print()` output
4. Blank line separator between sections

**Example structure:**
```python
# --------------------------------------------------
# N. TOPIC NAME: Brief Description
# --------------------------------------------------
# Implementation code
print()  # Separator
```

## Development Workflow

### Running the Project
Execute the entire demonstration suite:
```powershell
python loop_tasks.py
```
All examples run sequentially and print their output to console.

### Testing Changes
- Run the full script to verify loop logic produces expected output
- Check console output for formatting and correctness
- Verify each section produces distinct, readable output

## Key Patterns & Conventions

### Loop Constructs Demonstrated
1. **`range()`-based loops**: `for num in range(1, 101)`
2. **Conditional iteration**: Breaking/continuing within loops
3. **Nested loops**: Multiplication table example (section 5)
4. **String iteration**: Character-by-character looping (section 4)
5. **List iteration**: Accumulation patterns (section 8)

### Common Implementation Details
- **Section 1**: `range(1, 101)` shows 1-based ranges; output uses `end=" "` for single-line printing
- **Section 5**: Nested loops with formatted output using f-strings: `f"{i} x {j} = {i * j}"`
- **Section 8**: Accumulation pattern (`total += price`) with money formatting (`:.2f`)

## When Modifying Examples
- Preserve the section structure and numbering
- Keep explanatory comments intact
- Maintain output clarity (use `print()` after each section)
- Follow existing formatting conventions (no extra decorations beyond headers)

## Testing Hints
- Loop conditions: verify off-by-one errors in `range()` calls
- Accumulator patterns: ensure initial values and update logic
- Nested loops: check that inner loop resets/iterates correctly
- String iteration: verify character-by-character output is complete

## Reference Structure
See [loop_tasks.py](loop_tasks.py) for the complete implementation reference.
