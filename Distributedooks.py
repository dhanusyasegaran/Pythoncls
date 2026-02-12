def distribute_books_example(books, students, max_pages):
    student_assignments = [[] for _ in range(students)]
    current_student_idx = 0
    current_pages = 0

    for pages in books:
        # If adding this book exceeds the max_pages for the current student
        # AND we have more students available to assign to
        if current_pages + pages > max_pages and current_student_idx + 1 < students:
            current_student_idx += 1
            current_pages = pages
            student_assignments[current_student_idx].append(pages)
        # If adding this book exceeds the max_pages for the current student
        # BUT we don't have more students available (or pages > max_pages itself, which should be handled by initial checks)
        elif current_pages + pages > max_pages and current_student_idx + 1 >= students:
            # This case means it's not possible with this max_pages, but for demonstration,
            # we'll still show the distribution up to this point. In a real is_possible, this would return False.
            print(f"Cannot assign book {pages} to student {current_student_idx+1} without exceeding {max_pages} pages.")
            print("This scenario implies max_pages is too small or there aren't enough students.")
            return None
        else:
            current_pages += pages
            student_assignments[current_student_idx].append(pages)
            
    return student_assignments

books_example = [12, 34, 67, 90]
students_example = 2
minimum_max_pages = 113 # The result from allocate_books

assigned_books = distribute_books_example(books_example, students_example, minimum_max_pages)

if assigned_books:
    for i, assignment in enumerate(assigned_books):
        print(f"Student {i+1} reads books with pages: {assignment} (Total: {sum(assignment)})")
