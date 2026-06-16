% Facts

person(john, 25).
person(mary, 30).
person(david, 22).

% Pattern Matching Rule

match_person(Name, Age) :-
    person(Name, Age).
