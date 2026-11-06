"""Reproducible synthetic signup experiment. All records are fictional."""
import numpy as np
import pandas as pd
from scipy.stats import norm

def make_data(n=12000, seed=42, lift=0.20):
    """Synthetic randomized A/B test. lift is a relative conversion lift."""
    rng = np.random.default_rng(seed)
    variant = rng.integers(0, 2, size=n)
    device = rng.choice(["desktop", "mobile"], size=n, p=[0.4, 0.6])
    baseline = np.where(device == "mobile", 0.065, 0.105)
    probability = np.clip(baseline * (1 + lift * variant), 0, 1)
    converted = rng.binomial(1, probability)
    return pd.DataFrame({
        "visitor_id": [f"visitor_{i:05d}" for i in range(n)],
        "variant": np.where(variant == 1, "Treatment", "Control"),
        "device": device,
        "converted": converted,
    })

def summarize(df):
    result = df.groupby("variant")["converted"].agg(["sum", "count", "mean"])
    result = result.reindex(["Control", "Treatment"])
    return result

def compare(df):
    """Two-sided pooled z-test and unpooled normal-approximation CI for rate difference."""
    s = summarize(df)
    x0, x1 = s["sum"].to_numpy()
    n0, n1 = s["count"].to_numpy()
    p0, p1 = x0/n0, x1/n1
    pooled = (x0+x1)/(n0+n1)
    se_null = np.sqrt(pooled*(1-pooled)*(1/n0+1/n1))
    z = (p1-p0)/se_null if se_null > 0 else 0.0
    p_value = float(2*norm.sf(abs(z))) if se_null > 0 else 1.0
    se = np.sqrt(p0*(1-p0)/n0 + p1*(1-p1)/n1)
    ci = ((p1-p0)-1.96*se, (p1-p0)+1.96*se)
    return {"control_rate": float(p0), "treatment_rate": float(p1),
            "absolute_lift": float(p1-p0),
            "relative_lift": float((p1/p0-1) if p0 else np.nan),
            "p_value": p_value, "ci95": tuple(map(float, ci)),
            "n_control": int(n0), "n_treatment": int(n1)}
