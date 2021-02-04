import numpy as np

def construct_regressors(data,nBack):
    #Set empty regressors
    regressor_ch =  np.zeros((1,nBack))
    regressor_cxr = np.zeros((1,nBack))
    regressor_rew = np.zeros((1,nBack))
    nChoices = len(data)
    regressors = []

    #Update regregressors
    for choice in range(nChoices):
        #Which side was picked
        side = data.at[choice,'sides']

        #Fill in the regressor
        regressors.insert(choice, [regressor_cxr, regressor_ch, regressor_rew])

        """% These letter variables will be one iff the choice_i'th letter is their letter.
        Set them to zero, so that if it's a violation trial and they don't get set,
        they'll be halfway between their set values of -1 and 1"""

        #update reward history vectors
        #Don't understand
        reward = data.at[choice,'rewards']
        c = 0
        x = 0
        r = 0

        if side == 'l':
            if reward == 1:
                c = -1
                x = -1
                r = 1
            else:
                c = -1
                x = 1
                r = -1

        elif side == 'r':
            if reward == 1:
                c = 1
                x = 1
                r = 1
            else:
                c = 1
                x = -1
                r = -1

        elif side == 'v':
            continue

        #Add regressor to start of vector and remove last value
        regressor_ch = np.insert(regressor_ch, 0, c)
        regressor_cxr = np.insert(regressor_cxr, 0, x)
        regressor_rew = np.insert(regressor_rew, 0, r)

    return(regressors)
