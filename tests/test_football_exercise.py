'''Write a program that asks the user for the names of two football teams,
and the score of one team followed by the score of the other team.
Your program should output how many points each team gets (3 for a win,1 for a draw, 0 if they lose).'''
import pytest
import football_exercise

def test_calculate_points():
    assert football_exercise.calculate_points(0, 0) == (1, 1)

# We can also use the decorator pytest.mark.parametrize to test multiple cases. Note that we define the names of the
# parameters in the function definition, and then we use them in the call to the test function. Note also that we
# define a list of tuples, where each tuple contains the values for the parameters.
@pytest.mark.parametrize("score_t1, score_t2, points_t1, points_t2", [
    (1, 0, 3, 0),
    (0, 1, 0, 3),
    (1, 1, 1, 1)
])
def test_calculate_points(score_t1, score_t2, points_t1, points_t2):
    assert football_exercise.calculate_points(score_t1, score_t2) == (points_t1, points_t2)


# A test to catch the exception thrown by the function check_points.
def test_check_input_negative_fails():
    with pytest.raises(ValueError) as e_info:
        football_exercise.check_points(-1)
    assert str(e_info.value) == 'Invalid Score'