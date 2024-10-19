def swap_text(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
    
    middle_index_f1 = len(lines1) // 2
    last_line_f2 = lines2[-1]
    
    lines1[middle_index_f1], lines2[-1] = last_line_f2, lines1[middle_index_f1]
    
    with open(file1, 'w') as f1, open(file2, 'w') as f2:
        f1.writelines(lines1)
        f2.writelines(lines2)

swap_text("Wk 7\q6file1.txt", "Wk 7\q6file2.txt")