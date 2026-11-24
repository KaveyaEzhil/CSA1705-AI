bird(sparrow).
bird(parrot).
bird(pigeon).

can_fly(X) :- bird(X).

?- can_fly(sparrow).