# One-Dimensional Quantum Scattering; Unbound Particles

*Please have [MathJax Plugin for Github](https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima?hl=en) or similiar turned on to view $\LaTeX$.*

## The Problem
**The table below shows the dependence of the reflection coefficients on scattering energy. Determine the one-dimensional scattering potential. Use $m=1=\hbar$.**

  |  $R$ |  $E$  |
  :---: | :---:
  $1.00000$ | $1.8$
  $1.00000$ | $1.9$
  $1.00000$ | $2.0$
  $0.52319$ | $2.1$
  $0.39900$ | $2.2$
  $0.32312$ | $2.3$
  $\vdots$ | $\vdots$
  $0.11591$ | $3.0$
  $0.10260 $ | $3.1$
  $0.09107$ | $3.2$
  $\vdots$ | $\vdots$
  $0.01626$ | $4.8$
  $0.01469$ | $4.9$
  $0.01328$ | $5.0$
  
## The Solution
Using the energies and reflection coefficients above, the potentials $V$ corresponding to each $R$ and $E$ can be found using the step by step computational procedure below. 
\begin{align} 
  &k_1 = \sqrt{ \frac{2mE}{\hbar} }  \\\\\\
  &k_2 = k_1 \left( \frac{1-\sqrt{R}}{1+\sqrt{R}} \right) \\\\\\
  &V = E - \frac{\left(\hbar k_2\right)^2}{2m}
\end{align}

After all the potentials have been found, assume equal position spaceing between measurements. With this assumption plot out $V$ vs $x$.
<img src="https://github.com/spyderkam/1D-Unbound-Scattering/blob/main/fig1-1.png" alt="alt text" width="625" height="400">

It appears to be some polynomial function. Try curve fitting $V(x) = ax^3 + bx^2 + cx + d$; I used Python3's $\texttt{curve_fit}$ from the $\texttt{scipy.optimize}$ library.
