# Devoir Maison - Algorithmique avancée

###### Pierre Mével

## Programmation Dynamique

1.  Compréhension de l'algorithme proposé par D. Knuth.

Le problème proposé est celui de la recherche dans une arbre binaire non équilibré, créé spécifiquement pour améliorer le temps d'accès moyen en fonction des fréquences d'accès de chaque élément.

Pour cela, on associe à chacun des éléments i de notre liste d'élément une fréquence de rencontre `α[i]` et la fréquence `β[i]` de rencontrer un élément situé entre les éléments `i` et `i+1`.

On calcule ensuite le "poids" d'un arbre qui est la somme des produits des fréquences par les niveaux dans l'arbre, en sachant que sont ajoutées à l'arbre des positions terminales vides.

Ce poids peut être noté `P = Pl + Pr + W` où `Pr` et `Pl` sont les poids des sous arbres de droite et gauche, et `W` la somme de toutes les fréquences (puisque les sous arbres sont à un niveau plus bas).

**On note enfin que trouver un arbre de recherche optimal en temps d'accès moyen revient à minimiser P.**

On comprend bien que l'on peut utiliser la programmation dynamique pour répercuter le problème sur deux arbres plus petits, et itérer.

L'algorithme optimal réduit le nombre de calculs nécessaires en utilisant certaines nouvelles propriétés. Elles permettent de limiter la recherche de la racine R(i,j) de l'arbre optimal des éléments i à j à l'intervalle [R(i,j-1), R(i+1,j)].

2.  Pseudo-Code

_On utilise p et q car alpha et beta sont compliquées à obtenir en markdown_

```
ALGORITHM: Construction of an Optimal Binary Search Tree
    Given:
        A[1...n] elements to put in the tree

        p[1...n]: p[i] is the frequency of appearance of the element A[i]

    Computed:
        P[i,j]: for i and j in [1...n], is the weighted path length of the
        optimal binary tree with elements between A[i] and A[j]

        W[i,j]: for i and j in [1...n], is the weight of the tree,
        the sum of the frequencies p[k] and q[k] with k between i and j

        R[i,j]: for i and j in [1...n], is the index of the optimal root
        of the tree for elements between A[i] and A[j]

START:
    for k in [1...n] do:
        for i in [0...n-k] do:
            j = k + i
            P[i,j] =  INFINITY
            W[i,j] = W[i,j-1] + p[j]
            if k == 1 do: //first element
                R[i,j] = j
            end
            else do:
                for r in [R[i,j-1]...R[i+1,j]] do:
                    T <- W[i,j] + P[i, r-1] + P[r,j]
                    if T <= P[i,j] do:
                        R[i,j] <- r // Keep new optimal root
                        P[i,j] <- T // Keep new optimal cost
                    end
                end

                // Here we see why we have been using a descending order: we are
                // therefore sure that all P[i, r-1] and P[r,j] are already computed
                // and stored

            end
        end
    end
```
