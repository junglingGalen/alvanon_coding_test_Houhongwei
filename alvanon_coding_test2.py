from typing import List

"""
The number of goals achieved by two football teams in matches in a league is given in the form of two lists.
For each match of team B, compute the total number of matches of team A where team A has scored less than or equal to the number of goals scored by team B in that match. 
Example: 
    teamA = [1, 2, 3] 
    teamB = [2, 4] 
Team A has played three matches and has scored teamA = [1, 2, 3] goals in each match respectively. 
Team B has played two matches and has scored teamB = [2, 4] goals in each match respectively. 
For 2 goals scored by team B in its first match, team A has 2 matches with scores 1 and 2. 
For 4 goals scored by team B in its second match, team A has 3 matches with scores 1, 2 and 3. 
Hence, the answer is [2, 3]
"""


def football_count(teamA_scored: List, teamB_scored: List) -> List[int]:
    res = []
    for b_score in teamB_scored:
        cnt = 0
        for a_score in teamA_scored:
            if a_score <= b_score:
                cnt += 1
        res.append(cnt)
    return res


if __name__ == '__main__':
    test_input = [([], [1]), ([1], []), ([1, 2, 3], [2, 4]), ([], []), ([5, 8, 6, 7], [1, 5, 9, 3])]
    res_assert = [[0], [], [2, 3], [], [0, 1, 4, 0]]
    for i in range(len(test_input)):
        print(f"input：{test_input[i]}", f"output：{res_assert[i]}")
        assert res_assert[i] == football_count(*test_input[i])
    print("Congratulations you have passed!")
