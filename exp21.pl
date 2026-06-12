% Base Case
hanoi(1, Source, Destination, _) :-
    write('Move Disk 1 from '),
    write(Source),
    write(' to '),
    write(Destination), nl.

% Recursive Case
hanoi(N, Source, Destination, Auxiliary) :-
    N > 1,
    N1 is N - 1,

    hanoi(N1, Source, Auxiliary, Destination),

    write('Move Disk '),
    write(N),
    write(' from '),
    write(Source),
    write(' to '),
    write(Destination), nl,

    hanoi(N1, Auxiliary, Destination, Source).
