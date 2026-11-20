import math

def radial_distortion(r, k1):
    """径向畸变。"""
    raise NotImplementedError("TODO: radial_distortion")

def tangential_offset(x, y, p1, p2, r2):
    """切向畸变。"""
    raise NotImplementedError("TODO: tangential_offset")

def chromatic_scale(channel, base):
    """色差缩放。"""
    raise NotImplementedError("TODO: chromatic_scale")

def vignette(radius, strength):
    """暗角。"""
    raise NotImplementedError("TODO: vignette")

def distort_uv(uv, center, k1):
    """UV 畸变。"""
    raise NotImplementedError("TODO: distort_uv")

def inverse_iterations(error, threshold):
    """反变换迭代数。"""
    raise NotImplementedError("TODO: inverse_iterations")

def camera_params_key(camera_id):
    """相机参数键。"""
    raise NotImplementedError("TODO: camera_params_key")

def ui_passthrough(layer):
    """UI 透传。"""
    raise NotImplementedError("TODO: ui_passthrough")

def bloom_before_distort(order):
    """bloom 顺序。"""
    raise NotImplementedError("TODO: bloom_before_distort")

def dirt_uv(uv):
    """屏幕空间脏污。"""
    raise NotImplementedError("TODO: dirt_uv")

def aspect_radius(x, y, width, height):
    """宽幅半径。"""
    raise NotImplementedError("TODO: aspect_radius")

def channel_offset(channel, px, scale):
    """通道偏移。"""
    raise NotImplementedError("TODO: channel_offset")

def distortion_strength(resolution, base):
    """分辨率相关强度。"""
    raise NotImplementedError("TODO: distortion_strength")

def clamp_uv(uv):
    """UV 钳制。"""
    raise NotImplementedError("TODO: clamp_uv")

def degrade_chroma(quality):
    """降级保留色差。"""
    raise NotImplementedError("TODO: degrade_chroma")
