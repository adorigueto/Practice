import pandas as pd

def avg_percentage(game_id, ft_attempt_id, team, result):
    """
    :param game_id: (list) The ID of the game. 
    :param ft_attempt_id: (list) The ID of the free throw attempt for a given game.
    :param team: (list) Which team took the free throw.
    :param result: (list) The result of the free throw, which is either missed or made.
    :returns: (float) The mean value of the percentages (0.0-100.0) of free throws that
               each team scored in each game.
    """
    col = ['game_id', 'ft_attempt_id', 'team', 'result']
    df = pd.DataFrame({col[0]: game_id, col[1]: ft_attempt_id, col[2]: team, col[3]: result})
    df['ft_attempt_id'] = [1] * len(df['ft_attempt_id'])
    total_ft_per_team = df.groupby(['game_id', 'team']).sum()
    total_mades_per_team = df.groupby(['game_id', 'team']).sum()

    return

#For example, with the parameters below, the function should return 58.33
print(avg_percentage(
    [1, 1, 1, 1, 2, 2],
    [1, 2, 3, 4, 1, 2],
    ['home','home','away','home','away','home'],
    ['made','missed','made','missed','missed','made']
))

game_id = [1, 1, 1, 1, 2, 2]
ft_attempt_id = [1, 2, 3, 4, 1, 2]
team = ['home','home','away','home','away','home']
result = ['made','missed','made','missed','missed','made']
col = ['game_id', 'ft_attempt_id', 'team', 'result']
df = pd.DataFrame({col[0]: game_id, col[1]: ft_attempt_id, col[2]: team, col[3]: result})
df['ft_attempt_id'] = [1] * len(df['ft_attempt_id'])
total_ft_per_team = df.groupby(['game_id', 'team']).sum()
total_mades_per_team = df.groupby(['game_id', 'team']).sum()

total_ft_per_team['percentage'] = total_ft_per_team['ft_attempt_id'].mean()
total_ft_per_team

total_mades_per_team

cat = pd.Categorical(df['ft_attempt_id'])
cat
codes, uniques = pd.factorize(cat)
codes
result = [[uniques[0], df['grade'].groupby(df['class']).mean()[0].round()], uniques[1], df['grade'].groupby(df['class']).mean()[1].round()]
result
