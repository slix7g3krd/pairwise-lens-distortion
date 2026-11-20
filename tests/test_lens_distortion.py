import pytest
from render import lens_distortion as mod

CASES = [
    ("radial", 'm.radial_distortion(2, 0.1) == approx(1.4)'),
    ("tangential", 'm.tangential_offset(0, 0, 0.1, 0.2, 0) == (0.0, 0.0)'),
    ("chroma", 'm.chromatic_scale(1, 1) == approx(1.05)'),
    ("vignette", 'm.vignette(1, 0.2) == approx(0.8)'),
    ("distort", 'm.distort_uv((0.5, 0.5), (0.5, 0.5), 0.2) == approx((0.5, 0.5))'),
    ("iter", 'm.inverse_iterations(8, 1) == 3'),
    ("key", 'm.camera_params_key("L") == "L"'),
    ("ui", 'm.ui_passthrough("ui") is True'),
    ("bloom", 'm.bloom_before_distort("bloom-first") is True'),
    ("dirt", 'm.dirt_uv((1.25, -0.5)) == approx((0.25, 0.5))'),
    ("aspect", 'm.aspect_radius(960, 540, 1920, 1080) == approx(0.0)'),
    ("channel", 'm.channel_offset(1, 2, 0.5) == approx(1.0)'),
    ("strength", 'm.distortion_strength(2, 1) == approx(0.5)'),
    ("clamp", 'm.clamp_uv((-1, 2)) == (0.0, 1.0)'),
    ("degrade", 'm.degrade_chroma(1) is True')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
