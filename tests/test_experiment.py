from src.experiment import make_data, summarize, compare

def test_deterministic():
    assert make_data(seed=3).equals(make_data(seed=3))

def test_shape_and_schema():
    df = make_data(n=200)
    assert len(df) == 200
    assert set(df.columns) == {"visitor_id", "variant", "device", "converted"}
    assert df.visitor_id.is_unique
    assert set(df.converted.unique()).issubset({0, 1})

def test_comparison_and_ci():
    result = compare(make_data(n=12000))
    assert 0 <= result["p_value"] <= 1
    assert result["ci95"][0] <= result["absolute_lift"] <= result["ci95"][1]
    assert result["n_control"] + result["n_treatment"] == 12000

def test_summary():
    s = summarize(make_data(n=100))
    assert s["count"].sum() == 100
