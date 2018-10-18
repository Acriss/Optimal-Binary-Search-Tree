class OptimalTree:
    def __init__(self, P):
        self.P = P
        self.weight = [[0 for i in range(len(P))] for j in range(len(P))]
        self.cost = [[0 for i in range(len(P))] for j in range(len(P))]
        self.root = [[0 for i in range(len(P))] for j in range(len(P))]
        self.n = len(P)

    def initialize_calculations(self):
        for i in range(self.n):
            self.weight[i][i] = self.P[i]

        # Compute all the necessary sums, each time adding a new alpha + beta value
        for i in range(self.n):
            for j in range(i + 1, self.n):
                self.weight[i][j] = self.weight[i][j - 1] + self.P[j]

    def create_tree(self):
        self.initialize_calculations()

        # For single nodes, the only candidate as root is the element itself
        for i in range(self.n):
            self.root[i][i] = i
            self.cost[i][i] = self.P[i]

        for l in range(2, self.n + 1):
            for i in range(self.n - l + 1):
                # Trying to get Cost[i][j] and Root[i][j]

                j = i + l -1
                # Thanks to the ressources from this [article](http://www.inrg.csie.ntu.edu.tw/algorithm2014/presentation/Knuth71.pdf), we must only iterate between Root[i][j - 1] and Root[i +1][j]

                computed_weights = [(self.cost[i][k - 1] if k - 1 >= i else 0) + (self.cost[k + 1][j] if k + 1 <= j else 0)
                for k in range(self.root[i][j - 1], self.root[i + 1][j] + 1)]

                minimum_weight = min(computed_weights)
                minimum_root = computed_weights.index(minimum_weight) + self.root[i][j - 1]

                self.root[i][j] = minimum_root
                self.cost[i][j] = minimum_weight + self.weight[i][j]

    def get_parents_from_roots(self):
        # Here we are going to use the Root matrix and for each node of the tree we are building
        # We are going to retrieve the index of its parent on the optimal tree.

        parents = [-1] * len(self.root)
        self.build_sub_tree(parents, 0, len(self.root) - 1, -1)

        tree_root =  parents.index(-1)
        parents[tree_root] = tree_root
        return parents

    def build_sub_tree(self, parents, i, j, index):
        # Recursively build the tree from the root down to the leaves
        parents[self.root[i][j]] = index
        if (i < j):
            if (i <= self.root[i][j] - 1):
                self.build_sub_tree(parents, i, self.root[i][j] - 1, self.root[i][j])
            if (j >= self.root[i][j] + 1):
                self.build_sub_tree(parents, self.root[i][j] + 1, j, self.root[i][j])
