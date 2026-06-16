% Facts

male(john).
male(david).
male(mike).

female(mary).
female(linda).
female(susan).

% Parent Relationships

parent(john, david).
parent(mary, david).

parent(john, linda).
parent(mary, linda).

parent(david, mike).
parent(susan, mike).

% Rules

father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

grandfather(X, Y) :-
    father(X, Z),
    parent(Z, Y).

grandmother(X, Y) :-
    mother(X, Z),
    parent(Z, Y).

brother(X, Y) :-
    male(X),
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

sister(X, Y) :-
    female(X),
    parent(Z, X),
    parent(Z, Y),
    X \= Y.
