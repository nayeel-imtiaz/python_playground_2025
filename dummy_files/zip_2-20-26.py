names = ["John","Mike","Anna"]
scores = [90,85,95]

pairs = sorted(zip(scores, names))
print(f"{pairs}")

scores, names = zip(pairs)
print(f"scores: {scores}, names: {names}")