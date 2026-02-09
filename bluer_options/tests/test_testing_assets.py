list_of_assets = [
    {
        "things": 1,
    },
    {
        "things": [0, 1],
        "are_01": True,
        "are_ints": True,
    },
    {
        "things": [1, 2, 3],
        "are_ints": True,
        "are_positive_ints": True,
    },
    {
        "things": [1, -2, 3],
        "are_ints": True,
    },
    {
        "things": [1.0, 2.0, 3.0],
        "are_positive_floats": True,
    },
    {
        "things": [1.0, -2.0, 3.0],
    },
    {
        "things": "this",
    },
    {
        "things": {"this": "that"},
    },
    {
        "things": [{"this": "that"}],
    },
    {
        "things": ["this", ["that"]],
    },
    {
        "things": [],
        "are_01": True,
        "are_bools": True,
        "are_ints": True,
        "are_nonempty_strs": True,
        "are_positive_floats": True,
        "are_positive_ints": True,
        "are_strs": True,
        "is_list_of_str": True,
    },
    {
        "things": ["", "this"],
        "are_strs": True,
        "is_list_of_str": True,
    },
    {
        "things": ["this", "that"],
        "are_nonempty_strs": True,
        "are_strs": True,
        "is_list_of_str": True,
    },
    # += boolean
    {
        "things": True,
    },
    {
        "things": [0, 1, True],
        "are_01": True,
        "are_ints": True,
    },
    {
        "things": [True],
        "are_01": True,
        "are_bools": True,
        "are_ints": True,
        "are_positive_ints": True,
    },
    {
        "things": [False],
        "are_01": True,
        "are_bools": True,
        "are_ints": True,
    },
    {
        "things": [False, True],
        "are_01": True,
        "are_bools": True,
        "are_ints": True,
    },
    {
        "things": [1, 2, 3, True],
        "are_ints": True,
        "are_positive_ints": True,
    },
    {
        "things": [1, -2, 3, False],
        "are_ints": True,
    },
    {
        "things": [1.0, 2.0, 3.0, False],
    },
    {
        "things": [1.0, -2.0, 3.0, True],
    },
    {
        "things": {"this": 12},
        "is_a_flat_dict": 1,
    },
    {
        "things": {
            "this": 0,
            "that": 1,
        },
        "is_a_flat_dict": 1,
    },
    {
        "things": {"this": True},
        "is_a_flat_dict": 1,
    },
    {
        "things": [{"this": False}],
        "is_a_flat_dict": 1,
    },
    {
        "things": ["this", [True]],
    },
    {
        "things": ["", "this", True],
    },
    {
        "things": ["this", "that", False],
    },
]
