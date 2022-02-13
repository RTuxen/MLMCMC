# Multi-Level Markov Chain Monte Carlo estimation
Project in the [Computational Statistics](https://www11.ceda.polimi.it/schedaincarico/schedaincarico/controller/scheda_pubblica/SchedaPublic.do?&evn_default=evento&matricola=989644&c_insegn=055700) (055700) course at Politecnico di Milano.

Supervised by [Andrea Manzoni](https://www4.ceda.polimi.it/manifesti/manifesti/controller/ricerche/RicercaPerDocentiPublic.do?evn_didattica=evento&k_doc=189941&polij_device_category=DESKTOP&__pj0=0&__pj1=9619a602b442b2145bf9220580e36137)

Project uses the [MLDA sampler](https://docs.pymc.io/en/stable/pymc-examples/examples/samplers/MLDA_introduction.html) implemented in [PyMC3](https://docs.pymc.io/en/v3/)

## Collaborators
[Rasmus Tuxen](https://github.com/RTuxen)

[Simon Fredriksen](https://github.com/Slfredri)

[William Rom](https://github.com/William-Rom)

## Repository Structure

All the work done is in the form of jupyter Notebooks. They can be found in the *Notebooks/* folder. The methods are primarily applied to two simple ODE problems:
- An Oscillating Spring Problem
- A Lotka-Volterre Problem

## Experimental Results
In this project we show how MLMCMC techniques can be utilized to achieve a higher efficiency than the standard Metropolis sampler.
Below is show the Effective Sample Size (ESS) of a Metropolis sampler compared to different initializations of the MLMCMC sampler with
different depth and level coarsity:
![Alt text](figures/spring_problem_analytical_figures/dual_parameter_estimation/increasing_level_noise_test/ess.png?raw=true "Title")

Additionally we explore the effect of data density, data noise, prior distributions and proposal variance on simple ODE problems.
Below is shown an example of priors examined in the Spring problem 
![Alt text](figures/spring_problem_analytical_figures/dual_parameter_estimation/Prior_distribution_test/prior_distributions.png?raw=true "Title")


## References
J. P. Madrigal-Cianci, F. Nobile, R. Tempone: Analysis of a class of Multi-Level Markov Chain Monte Carlo algorithms based on Independent Metropolis-Hastings, [https://arxiv.org/abs/2105.02035](https://arxiv.org/abs/2105.02035)

T.J. Dodwell, C. Ketelsen, R. Scheichl, A.L. Teckentrup: A Hierarchical Multilevel Markov Chain Monte Carlo Algorithm with Applications to Uncertainty Quantification in Subsurface Flow, [https://arxiv.org/abs/1303.7343](https://arxiv.org/abs/1303.7343)
