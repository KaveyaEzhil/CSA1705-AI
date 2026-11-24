% Facts
likes(john, X) :- food(X).

food(apple).
food(vegetable).

eats(anil, peanuts).
alive(anil).

% Rules
food(X) :-
    eats(Y, X),
    alive(Y).

eats(harry, X) :-
    eats(anil, X).

likes(john, peanuts).