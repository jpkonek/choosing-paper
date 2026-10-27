"""Shared T1 geometry for D1 (NUMERICS helpers only)."""
import numpy as np

E = np.eye(3)


def T1(eps):
    c0 = (1 - eps) / 3
    return [c0 * np.ones(3) + eps * E[k] for k in range(3)]


def kappa(eps):
    return (1 + 2 * eps) / (1 - eps)


def corner_ray(V, k, j):
    """corner ray r_kj = F_k cap F_j, oriented so that it is >= 0 on T."""
    r = np.cross(V[k], V[j])
    l = 3 - k - j
    return r if r @ V[l] > 0 else -r


def P(K, g):
    """lower prevision of g on the convex hull of the points K (list of probability vectors)."""
    return min(m @ g for m in K)


def Pbar(K, g):
    return max(m @ g for m in K)


def tangent_point(V, i, j, eps):
    """o_ij = line(v_i, e_j) cap line(v_j, e_i) (outer vertex of the tangent hexagon)."""
    # solve v_i + a (e_j - v_i) = v_j + b (e_i - v_j)
    A = np.vstack([E[j] - V[i], -(E[i] - V[j])]).T
    ab, *_ = np.linalg.lstsq(A, V[j] - V[i], rcond=None)
    return V[i] + ab[0] * (E[j] - V[i])


def facet_param(V, k):
    """facet F_k from r_{k i} to r_{k j} with i<j the other indices; returns h(tau)."""
    i, j = [x for x in range(3) if x != k]
    r0, r1 = corner_ray(V, k, i), corner_ray(V, k, j)
    return lambda t: (1 - t) * r0 + t * r1, r0, r1
