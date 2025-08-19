import os

def test_matching_files_exist():
    clinical = "assets/clinical_eda_graphs/updrs_by_exercise.png"
    preclinical = "assets/preclinical_images/Locomotor_Activity2.png"
    assert os.path.exists(clinical), "Clinical image missing"
    assert os.path.exists(preclinical), "Preclinical image missing"
