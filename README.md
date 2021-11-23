# Multi-Level Markov Chain Monte Carlo estimation
Project in the [Computational Statistics](https://www11.ceda.polimi.it/schedaincarico/schedaincarico/controller/scheda_pubblica/SchedaPublic.do?&evn_default=evento&matricola=989644&c_insegn=055700) (055700) course at Politecnico di Milano.

Supervised by [Andrea Manzoni](https://www4.ceda.polimi.it/manifesti/manifesti/controller/ricerche/RicercaPerDocentiPublic.do?evn_didattica=evento&k_doc=189941&polij_device_category=DESKTOP&__pj0=0&__pj1=9619a602b442b2145bf9220580e36137)

## Collaborators
[Rasmus Tuxen](https://github.com/RTuxen)

[Simon Fredriksen](https://github.com/Slfredri)

[William Rom](https://www.google.com/)


### Notes
- We will primarily work with time-dependent ODE's

- Look at the example codes and really understand them.
Then check out if it works in google colab.
Start out with easy examples of time dependent diff eq: like  ay' = b*y, dx(t)/dt = a(t)x(t).

- Use different time durations T and different sampling rates dt to generate data then add some noise.
Hide the coefficients and use the MLMCMC solver on the problem. Compare the MAP estimate of the coefficients to the problem

- Look into creating examples using Lotka–Volterra equations (set parameters for data generation+noise and then hide coeffients and 
let the model figure them out)