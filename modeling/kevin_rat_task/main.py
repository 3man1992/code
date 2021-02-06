#External imports
import statsmodels.api as sm
from statsmodels.formula.api import glm
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# pd.set_option("display.max_rows", None, "display.max_columns", None)

#My imports
from import_data import load_data
from construct_regressors import construct_regressors

#LOAD DATA
rat_data_file = "/Users/laurence/Desktop/Neuroscience/mproject/data/modeling_workflow_example/ratdata.mat"
data = load_data(rat_data_file)

"""Choices / Code to convert choices into binary to solve concat error"""
"""Only analyze trials that are non-vilations and of free choice."""
good_trials = data.loc[(data["sides"] == "l") | (data["sides"] == "r")]
good_trials = data.loc[(data["trial_types"] == "f")]
choices = np.asarray(good_trials["sides"])
for choice in range(len(choices)):
    if choices[choice] == "l":
        choices[choice] = 0
    elif choices[choice] == "r":
        choices[choice] = 1
    elif choices[choice] == "v": #Will need to remove this code
        choices[choice] = 0
        print("Error, violation trials should have been removed")
    else:
        print("Error, something happened that did not adhere to the choice logic", choices[choice])
choices = np.array(choices, dtype=np.float)

"""Reduce the regressors to only include the good trials"""
regressors = construct_regressors(data, 10)
# regessors = regressors.astype(int)
regressors = pd.DataFrame(regressors)
index_of_good_trials = good_trials.index.values
regressors = regressors[regressors.index.isin(good_trials.index)]
X = sm.add_constant(regressors, prepend=False)

"""GLM functions"""
model = sm.GLM(choices, X, family = sm.families.Binomial()).fit()
weights = model.params
weights = weights[:-1]
weights.index = weights.index + 1
reward_seeking_weights = weights[:10]
choice_weights = weights[10:20].reset_index(drop=True)
choice_weights.index += 1
outcome_weights = weights[20:30].reset_index(drop=True)
outcome_weights.index += 1
# print(reward_seeking_weights)
# print(choice_weights)
# print(outcome_weights)
# print(model.summary())

"""Plotting graphs"""
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)
ax1.plot(reward_seeking_weights)
ax1.set(title="Reward Seeking - Interaction term", ylabel="Regression Weights", xlabel="Trials in the past")
ax1.set_xlim(10,1)
ax1.set_ylim(-0.1,1.2)
ax2.plot(choice_weights)
ax2.set(title="Choice Perseveration", ylabel="Regression Weights", xlabel="Trials in the past")
ax2.set_xlim(10,1)
ax2.set_ylim(-0.1,1.2)
ax3.plot(outcome_weights)
ax3.set(title="Main Effect of Outcome", ylabel="Regression Weights", xlabel="Trials in the past")
ax3.set_xlim(10,1)
ax3.set_ylim(-0.1,1.2)
plt.show()

"""Data exploration"""
#Explore data types
# print("")
# print("Choices")
# print("-------")
# print("Choices is of type:", type(choices))
# print("Choices if of dtype:", choices.dtype)
# print("")
# print("Regressors")
# print("-------")
# print("Regressors is of type:", type(regressors))
# print("Regressors is of type:", regressors.dtype)
