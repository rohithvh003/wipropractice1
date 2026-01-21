
def student_generator(students):
    for s in students:
        yield f"{s.pid} - {s.name}"


def faculty_generator(faculty_list):
    for f in faculty_list:
        yield f"{f.fid} - {f.name}"