# Excel Rule Agent

AI-powered Excel template generator that allows non-technical users to define business transformation rules using natural language.

The system converts business instructions into structured rules and automatically generates transformed Excel templates.

---

## Problem

Business users frequently request custom template generation logic:

- If SKU equals a specific value
- Generate additional rows
- Replace only selected columns
- Preserve all remaining fields

Traditional solutions require modifying VBA or hardcoding logic.

This project moves rule creation to natural language.

---

## Solution

Users describe rules in plain English.

Example:

If SKU equals ABC
Generate:
SKU=Envelope

Generate:
SKU=DEL/EVRI

The system:

1. Converts instructions into structured JSON
2. Stores reusable rules
3. Reads Excel templates
4. Generates transformed output automatically

---

## Example

Input:

| SKU | Envelope |
|------|----------|
| ABC | EFG |

Rule:

If SKU equals ABC

Generate:
SKU=Envelope

Generate:
SKU=DEL/EVRI

Output:

| SKU | 
|------|
| ABC |
| DEF |
| DEL/EVRI |

---
