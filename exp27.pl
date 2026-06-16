% Graph Representation
edge(a, b, 4).
edge(a, c, 2).
edge(b, d, 5).
edge(c, e, 3).
edge(d, goal, 1).
edge(e, goal, 2).

% Heuristic Values
heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 2).
heuristic(d, 1).
heuristic(e, 1).
heuristic(goal, 0).

% Goal State
best_first(goal) :-
    write('Goal Reached'), nl.

best_first(Node) :-
    write('Visited: '), write(Node), nl,
    findall(H-Next,
            (edge(Node, Next, _), heuristic(Next, H)),
            Children),
    sort(Children, Sorted),
    Sorted = [_-BestNode | _],
    best_first(BestNode).
