student(101, Arun).
student(102, Bala).
student(103, Kavi).

teacher(T1, John).
teacher(T2, Mary).

subject(CS101, Python).
subject(CS102, Java).
subject(CS103, Prolog).

teaches(T1, CS101).
teaches(T2, CS102).
teaches(T1, CS103).

display_student :-
    student(ID, Name),
    write(ID), write(' '),
    write(Name), nl,
    fail.

display_student.