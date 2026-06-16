% Facts

fruit(apple, red).
fruit(banana, yellow).
fruit(grapes, green).
fruit(orange, orange).
fruit(mango, yellow).
fruit(cherry, red).

% Rule

color(Fruit, Color) :-
    fruit(Fruit, Color).
