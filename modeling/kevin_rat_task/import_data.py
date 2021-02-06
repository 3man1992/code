from scipy.io import loadmat
import pandas as pd
import numpy as np

"""Information on the data:

- dtype=[('sides', 'O'), ('rewards', 'O'), ('left_prob1', 'O'), ('right_prob1', 'O'), ('trial_types', 'O'), ('ratname', 'O'), ('nTrials', 'O')])}
- dict_keys(['__header__', '__version__', '__globals__', 'ratdata'])"""

#Function to load rat data from matlab struct to python
def load_data(file):
    mat_dict = loadmat(file)

    #Variables
    sides = [[row for row in line] for line in mat_dict["ratdata"][0][0]["sides"]]
    rewards = [[row.flat[0] for row in line] for line in mat_dict["ratdata"][0][0]["rewards"]]
    left_prob = [[row.flat[0] for row in line] for line in mat_dict["ratdata"][0][0]["left_prob1"]]
    right_prob = [[row.flat[0] for row in line] for line in mat_dict["ratdata"][0][0]["right_prob1"]]
    trial_types = [[row for row in line] for line in mat_dict["ratdata"][0][0]["trial_types"]]

    #Flatten lists
    sides = [item for sublist in sides for item in sublist]
    rewards = [item for sublist in rewards for item in sublist]
    left_prob = [item for sublist in left_prob for item in sublist]
    right_prob = [item for sublist in right_prob for item in sublist]
    trial_types = [item for sublist in trial_types for item in sublist]

    #Convert to data frame
    rat_df = pd.DataFrame([sides,rewards,left_prob,right_prob,trial_types]).T
    rat_df.columns = ["sides", "rewards", "left_prob", "right_prob", "trial_types"]
    # rat_df.apply(lambda(x))

    #nTrials should equal 12324
    assert len(rat_df) == 12324, "Data length not as expected"

    return rat_df
