import time as time
import warnings

import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm

warnings.filterwarnings("ignore")


#%% Generate data
RANDOM_SEED = 915623497
np.random.seed(RANDOM_SEED)

true_intercept = 1
true_slope = 2
sigma = 1

size = 200
x = np.linspace(0, 1, size)
y = true_intercept + true_slope * x + np.random.normal(0, sigma ** 2, size)

# Plot the data
fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111, xlabel="x", ylabel="y", title="Generated data and underlying model")
ax.plot(x, y, "x", label="sampled data")
ax.plot(x, true_intercept + true_slope * x, label="true regression line", lw=2.0)
plt.legend(loc=0)
plt.show()


#%% Define model
# Constructing the fine model
with pm.Model() as fine_model:
    # Define priors
    intercept = pm.Normal("intercept", 0, sigma=20)
    slope = pm.Normal("slope", 0, sigma=20)

    # Define likelihood
    likelihood = pm.Normal("y", mu=intercept + slope * x, sigma=sigma, observed=y)
    

#%% Define a coarse model
# Thinning the data set
x_coarse = x[::2]
y_coarse = y[::2]


# Constructing the coarse model
with pm.Model() as coarse_model:
    # Define priors
    intercept = pm.Normal("intercept", 0, sigma=20)
    slope = pm.Normal("slope", 0, sigma=20)

    # Define likelihood
    likelihood = pm.Normal("y", mu=intercept + slope * x_coarse, sigma=sigma, observed=y_coarse)
    
    
#%% Draw MCMC samples from the posterior using MLDA 
with fine_model:
    # Initialise step methods
    step = pm.MLDA(coarse_models=[coarse_model], subsampling_rates=[10])
    step_2 = pm.Metropolis()
    step_3 = pm.DEMetropolisZ()

    # Sample using MLDA
    t_start = time.time()
    trace = pm.sample(draws=6000, chains=4, tune=2000, step=step, random_seed=RANDOM_SEED)
    runtime = time.time() - t_start

    # Sample using Metropolis
    t_start = time.time()
    trace_2 = pm.sample(draws=6000, chains=4, tune=2000, step=step_2, random_seed=RANDOM_SEED)
    runtime_2 = time.time() - t_start

    # Sample using DEMetropolisZ
    t_start = time.time()
    trace_3 = pm.sample(draws=6000, chains=4, tune=2000, step=step_3, random_seed=RANDOM_SEED)
    runtime_3 = time.time() - t_start
    
# Trace plots
az.plot_trace(trace)
az.plot_trace(trace_2)
az.plot_trace(trace_3)