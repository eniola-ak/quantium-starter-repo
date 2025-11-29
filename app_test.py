from Visualizer import app
def test_header(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.wait_for_element("#header-one", timeout=120)
    assert header is not None
    assert header.text == "Pink Morsels Sales Data"

def test_visualization(dash_duo):
    dash_duo.start_server(app)
    figure = dash_duo.wait_for_element("#sales-graph", timeout=120)
    assert figure is not None

def test_region_picker(dash_duo):
    dash_duo.start_server(app)
    region_p = dash_duo.wait_for_element("#radio", timeout=120)
    assert region_p is not None