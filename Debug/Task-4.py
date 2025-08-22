# --- Step 1: Import Libraries ---
import pandas as pd
import numpy as np

# --- Step 2: Load Dataset ---
# Make sure you have uploaded "Online Retail.xlsx"
data = pd.read_csv('venv/OnlineRetail.csv', encoding ='ISO-8859-1')

# --- Step 3: Data Cleaning ---
data.dropna(inplace=True)                                       # remove nulls
data = data[~data['InvoiceNo'].astype(str).str.startswith('C')] # remove cancelled invoices
data = data[data['Quantity'] > 0]                               # keep only positive quantity


# --- Step 4: Prepare Transaction Dataset ---
# Group transactions by InvoiceNo into list of items
transactions = (data.groupby("InvoiceNo")['Description']
                .apply(list)
                .tolist())

print("Sample Transaction:", transactions[0][:10])  # show first 10 items of first invoice


# --- Step 5: Support Calculation Function ---
def get_support(itemset, transactions):
    """
    Calculate support of an itemset
    """
    count = 0
    for trans in transactions:
        if set(itemset).issubset(set(trans)):
            count += 1
    return count / len(transactions)


# --- Step 6: Candidate Generation ---
def generate_candidates(prev_frequent_itemsets, k):
    """
    Generate candidate itemsets of size k from frequent itemsets of size (k-1).
    """
    candidates = []
    prev_items = list(prev_frequent_itemsets.keys())

    for i in range(len(prev_items)):
        for j in range(i+1, len(prev_items)):
            # Union of two sets
            union_set = tuple(sorted(set(prev_items[i]) | set(prev_items[j])))
            if len(union_set) == k and union_set not in candidates:
                candidates.append(union_set)
    return candidates





# --- Step 7: Apriori Algorithm ---
def apriori(transactions, min_support=0.01):
    """
    Apriori algorithm implemented from scratch.
    Returns dict of frequent itemsets with their support.
    """
    item_support = {}
    num_trans = len(transactions)

    # Step 1: Get frequent 1-itemsets
    items = set(i for trans in transactions for i in trans)
    freq_itemsets = {}

    for item in items:
        sup = get_support([item], transactions)
        if sup >= min_support:
            freq_itemsets[(item,)] = sup

    all_freq_itemsets = dict(freq_itemsets)

    k = 2
    while freq_itemsets:
        # Step 2: Generate candidates of size k
        candidates = generate_candidates(freq_itemsets, k)

        freq_itemsets = {}
        for cand in candidates:
            sup = get_support(cand, transactions)
            if sup >= min_support:
                freq_itemsets[cand] = sup

        all_freq_itemsets.update(freq_itemsets)
        k += 1

    return all_freq_itemsets
# --- Step 8: Run Apriori ---
frequent_itemsets = apriori(transactions, min_support=0.02)

print("\nTop Frequent Itemsets:")
for item, sup in sorted(frequent_itemsets.items(), key=lambda x: -x[1])[:10]:
    print(item, ":", round(sup, 4))

# Function to generate rules from frequent itemsets

def generate_rules(frequent_itemsets, min_confidence):
    rules = []

    for itemset, support in frequent_itemsets.items():
        if len(itemset) > 1:
            # split into all possible A → B
            n = len(itemset)
            for i in range(n):
                for j in range(i+1, n):
                    A = tuple([itemset[i]])
                    B = tuple(sorted(set(itemset) - set(A)))

                    support_AB = support
                    support_A = frequent_itemsets.get(A, 0)
                    if support_A > 0:
                        confidence = support_AB / support_A
                        if confidence >= min_confidence:
                            rules.append((A, B, support_AB, confidence))
    return sorted(rules, key=lambda x: x[3], reverse=True)
# Output the final results
# Optional: Add visualizations
# Run Apriori
# --- Step 9: Association Rule Generation ---
def generate_rules(frequent_itemsets, transactions, min_conf=0.5):
    """
    Generate association rules from frequent itemsets.
    """
    rules = []
    for itemset, sup in frequent_itemsets.items():
        if len(itemset) < 2:
            continue
        for i in range(len(itemset)):
            antecedent = (itemset[i],)
            consequent = tuple(sorted(set(itemset) - set(antecedent)))

            support_ab = sup
            support_a = get_support(antecedent, transactions)
            support_b = get_support(consequent, transactions)

            confidence = support_ab / support_a if support_a > 0 else 0
            lift = confidence / support_b if support_b > 0 else 0

            if confidence >= min_conf:
                rules.append({
                    "antecedent": antecedent,
                    "consequent": consequent,
                    "support": round(support_ab, 4),
                    "confidence": round(confidence, 4),
                    "lift": round(lift, 4)
                })
    return pd.DataFrame(rules)


rules_df = generate_rules(frequent_itemsets, transactions, min_conf=0.5)

print("\nTop Association Rules:")
print(rules_df.head())
