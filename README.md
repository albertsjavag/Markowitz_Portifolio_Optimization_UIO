# Markowitz_Portifolio_Optimization_UIO
This is a repo used for portifolio optimization. 

## Author
Albert Sjåvåg 
Quantitative Finance | University of Oslo
Email: albert.sjaavaag@gmail.com

Github repo link: https://github.com/albertsjavag/Markowitz_Portifolio_Optimization_UIO


### Analytical solution for expected return
Let \( r_{i,t} \) denote the return of asset \( i \) at time \( t \).
The expected return is defined as the time average of historical returns:

$$
\langle r_i \rangle
= \frac{1}{T} \sum_{t=1}^{T} r_{i,t}
$$

For daily return data, the annualized expected return is given by

$$
\mu_i
= 252 \cdot \langle r_i \rangle
= 252 \cdot \frac{1}{T} \sum_{t=1}^{T} r_{i,t}
$$

Collecting the expected returns for all assets yields the expected return vector

$$
\boldsymbol{\mu}
=
\begin{pmatrix}
\mu_1 \\
\mu_2 \\
\vdots \\
\mu_N
\end{pmatrix}
$$



