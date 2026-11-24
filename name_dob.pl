person(Arun, '2002-05-10').
person(Bala, '2003-08-15').
person(Kavi, '2004-01-20').
person(Ravi, '2001-12-25').

display :-
    person(Name, DOB),
    write(Name), write(' - '),
    write(DOB), nl,
    fail.

display.