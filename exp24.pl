% Disease and Recommended Diet

diet(diabetes, 'Low sugar diet').
diet(hypertension, 'Low salt diet').
diet(obesity, 'Low calorie diet').
diet(anemia, 'Iron rich diet').
diet(heart_disease, 'Low fat diet').
diet(kidney_disease, 'Low protein diet').

% Rule

suggest_diet(Disease, Diet) :-
    diet(Disease, Diet).
