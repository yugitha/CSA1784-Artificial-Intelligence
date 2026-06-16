% Facts

has_feathers(tweety).
lays_eggs(tweety).

% Rules

bird(X) :-
    has_feathers(X).

bird(X) :-
    lays_eggs(X).

can_fly(X) :-
    bird(X).

% Goal

backward_chain(X) :-
    can_fly(X).
