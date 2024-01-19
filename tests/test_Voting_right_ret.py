import unittest

import pytest
import Voting_right_ret

@pytest.mark.parametrize("age, ret, vote", (
        (18, 47, True),
        (15, 50, False),
        (25, 40, True)
))
def test_Voting_right_ret(age, ret, vote ):
    assert Voting_right_ret.age_until_ret(age) == (ret,vote)


@pytest.mark.parametrize("age_1, pre_ret, pre_ret_percent", (
        (18, 42, None),
        (62, -2, 76),
        (70, -10, 100)
))
def test_Voting_right_ret(age_1, pre_ret, pre_ret_percent):
    assert Voting_right_ret.pre_ret(age_1) == (pre_ret, pre_ret_percent)

@pytest.mark.parametrize("age, legal_age", (
        (18, True),
        (15, False),
        (25, True)
))
def test_Voting_right_ret(age,legal_age):
    assert Voting_right_ret.drinking_age(age) == (legal_age)