import os
import pytest

def test_preclinical_images_exist():
    img_folder = "assets/preclinical_images"
    required_files = [
        "Setup_Design.png", "Setup.png",
        "HPLC_results1.png", "HPLC_results2.png",
        "Locomotor_Activity1.png", "Locomotor_Activity2.png",
        "Rotarod_Activity1.png", "Rotarod_Activity2.png"
    ]
    for img in required_files:
        assert os.path.exists(os.path.join(img_folder, img)), f"Missing: {img}"

def test_image_format():
    assert "png" in os.listdir("assets/preclinical_images")[0], "Not a PNG"
