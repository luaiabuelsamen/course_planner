import argparse
from docx import Document
import re

def extract_table_contents(table):
    table_data = []
    for row in table.rows:
        row_data = [cell.text.strip() for cell in row.cells]
        for idx, cell_text in enumerate(row_data):
            if '\t' in cell_text:
                split = cell_text.split('\t')
                row_data[idx] = split[idx]
            else:
                row_data[idx] = cell_text
        table_data.append(row_data)
    return table_data

def parse_courses(table_data):
    courses = []
    current_course = {}
    term = 0
    for row in table_data:
        current_course = {}
        if len(row) > 0:
            if "Term" in row[0]:
                term += 1
            else:
                current_course['course_code'] = row[0]
                current_course['course_name'] = row[1]
                current_course['credits'] = int(row[2])
                current_course['prerequisites'] = []
                current_course['corequisites'] = []
                current_course['term'] = term
                pattern = r'P\s*-([^\n/]+)(?:\s*/\s*P\s*or\s*C\s*-\s*([^\n/]+))?'

                matches = re.finditer(pattern, row[3])
                prerequisite_courses = []
                corequisite_courses = []
                for match in matches:
                    prerequisites = match.group(1).strip()
                    corequisites = match.group(2)
                    if corequisites:
                        corequisites = corequisites.strip()
                    prerequisite_courses = re.split(r'\s*(?:,|\bor\b)\s*', prerequisites)
                    corequisite_courses = re.split(r'\s*(?:,|\bor\b)\s*', corequisites) if corequisites else []
                    current_course['prerequisites'] = prerequisite_courses
                    current_course['corequisites'] = corequisite_courses
                courses.append(current_course)
    return courses

def main(file_path):
    doc = Document(file_path)
    tables = doc.tables

    if len(tables) > 0:
        all_table_data = []
        for table in tables:
            table_data = extract_table_contents(table)
            all_table_data.extend(table_data)
        
        courses = parse_courses(all_table_data)

        for course in courses:
            print("Course Code:", course['course_code'])
            print("Course Name:", course['course_name'])
            print("Credits:", course['credits'])
            print("Prerequisites:", ', '.join(course['prerequisites']))
            print("Corequisites:", ', '.join(course['corequisites']))
            print("\n")
    else:
        print("No tables found in the document.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract and parse course information from a curriculum table.")
    parser.add_argument("file_path", help="Path to the Word file containing the curriculum table.")
    args = parser.parse_args()
    
    main(args.file_path)
