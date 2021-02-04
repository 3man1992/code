#External imports
import statsmodels.api as sm
import numpy as np
from statsmodels.formula.api import glm

#My imports
from import_data import load_data
from construct_regressors import construct_regressors

# pd.set_option("display.max_rows", None, "display.max_columns", None)

#Create regressors
rat_data_file = "/Users/laurence/Desktop/Neuroscience/mproject/data/modeling_workflow_example/ratdata.mat"
data = load_data(rat_data_file)
regressors = construct_regressors(data, 10)

#Outline inputs to GLM
X = sm.add_constant(regressors, prepend=False)
choices = np.asarray(data["sides"])
assert len(choices) == 12324, "Choice length not as expected"

#Set family for GLM model
link_function = sm.families.links.logit
model_family = sm.families.Binomial(link = link_function)

#GLM functions
model = sm.GLM(choices, X, model_family)
results = model.fit()
print(model.summary())
