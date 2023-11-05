from question3 import make_oven, alchemy_combine

def test_alchemy_combine():
    assert alchemy_combine(
        make_oven(),
        ["lead", "mercury"],
        5000
    ) == "gold"

    assert alchemy_combine(
        make_oven(),
        ["water", "air"],
        -100
    ) == "snow"

    assert alchemy_combine(
        make_oven(),
        ["cheese", "dough", "tomato"],
        150
    ) == "pizza"

# Usually, you would have this part to run the tests if the file is executed directly
if __name__ == "__main__":
    test_alchemy_combine()
    print("All tests passed!")
