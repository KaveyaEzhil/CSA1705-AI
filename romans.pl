% Facts
man(marcus).
pompeian(marcus).
ruler(caesar).

% Rules
roman(X) :-
    pompeian(X).

person(X) :-
    man(X).

person(X) :-
    roman(X).

% Everyone is loyal to someone
loyal_to(X, someone) :-
    person(X).

% Marcus tried to assassinate Caesar
tries_assassinate(marcus, caesar).

% People try to assassinate only rulers
% to whom they are not loyal
not_loyal_to(X, Y) :-
    tries_assassinate(X, Y),
    ruler(Y).

% All Romans are either loyal to Caesar or hate him
hates(X, caesar) :-
    roman(X),
    not_loyal_to(X, caesar).