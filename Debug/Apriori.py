from itertools import combinations

# Dataset (transactions)
transactions = {
    100: [1, 3, 4],
    200: [2, 3, 5],
    300: [1, 2, 3, 5],
    400: [2, 5]
}

# Parameters
min_support = 2
min_confidence = 0.0  # we want all rules (filter later if needed)

# Step 1: Count support for single items (C1)
def get_support(itemset, transactions):
    count = 0
    for tid, items in transactions.items():
        if set(itemset).issubset(set(items)):
            count += 1
    return count

# Step 2: Generate candidates
def generate_candidates(prev_frequent, k):
    candidates = []
    items = list(set([i for s in prev_frequent for i in s]))
    items.sort()
    for comb in combinations(items, k):
        candidates.append(comb)
    return candidates

# Step 3: Apriori algorithm
frequent_itemsets = {}
k = 1

# C1 -> L1
candidates = generate_candidates([tuple([i]) for i in set(i for t in transactions.values() for i in t)], k)
L = []
for c in candidates:
    sup = get_support(c, transactions)
    if sup >= min_support:
        L.append((c, sup))
frequent_itemsets[k] = L

# Generate further
while frequent_itemsets[k]:
    k += 1
    prev_frequent = [x[0] for x in frequent_itemsets[k-1]]
    candidates = []
    # Join step
    for comb in combinations(set(i for s in prev_frequent for i in s), k):
        candidates.append(comb)

    L = []
    for c in candidates:
        sup = get_support(c, transactions)
        if sup >= min_support:
            L.append((c, sup))
    frequent_itemsets[k] = L

# Remove last empty
if not frequent_itemsets[k]:
    del frequent_itemsets[k]


# Print Frequent Itemsets
print("Frequent Itemsets:")
for k, itemsets in frequent_itemsets.items():
    for itemset, sup in itemsets:
        print(f"{itemset} -> support = {sup}")

# Step 4: Association Rules
print("\nAssociation Rules:")
rules = []
for k, itemsets in frequent_itemsets.items():
    for itemset, sup_count in itemsets:
        if len(itemset) > 2:
            for i in range(1, len(itemset)):
                for lhs in combinations(itemset, i):
                    rhs = tuple(sorted(set(itemset) - set(lhs)))
                    lhs_support = get_support(lhs, transactions)
                    conf = sup_count / lhs_support
                    rules.append((lhs, rhs, sup_count, conf))

# Format Output same as slide
for lhs, rhs, sup, conf in rules:
    lhs_str = "^".join(map(str, lhs))
    rhs_str = "^".join(map(str, rhs))
    print(f"{lhs_str} -> {rhs_str}, Support={sup}, Confidence={sup}/{get_support(lhs, transactions)} = {conf:.2f}, {conf*100:.0f}%")
