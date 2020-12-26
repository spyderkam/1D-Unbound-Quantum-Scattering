#!/usr/bin/env julia

using Plots
using Plots.Measures
using DelimitedFiles

ħ, m = 1, 1

K1(E) = sqrt(2*m*E / ħ)
K2(k1, R) = k1*((1-sqrt(R))/(1+sqrt(R)))
V0(E, k2) = E - (ħ*k2)^2/(2*m)

file = readdlm("path/to/scat.txt")
E = file[:, 1]
R = file[:, 2]

k1 = []     # initialize k1
V = []      # initialize V
for i in eachindex(E)
    append!(k1, K1(E[i]))
    append!(V, V0(E[i], K2(k1[i], R[i])))
end

T = []
for r in R
    append!(T, 1 - r)
end


# now plotting
um = [0, 1]
ok = [1, 1]

plot(um , ok, color="blue")
plot!(E ./ V, R, color="blue", left_margin=4mm)
plot_ref = plot!(E ./ V, T, color="red", legend=false, grid="off")
#savefig(plot_ref, "bounded_V.pdf")
