import filedata


def assert_parsed(data, parsed):
    print(filedata.dumps(parsed))
    assert data.expected == parsed


def test_parse_route_data(bird, data_parse_routes):
    data = data_parse_routes
    assert_parsed(data, bird._parse_route_data_v2(data.input))