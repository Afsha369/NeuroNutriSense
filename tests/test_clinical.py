import os

def test_clinical_graphs_present():
    files = os.listdir("assets/clinical_eda_graphs")
    expected = [
        "disease_progression_vs_years.png", "updrs_by_exercise.png",
        "pairplot_medication_progression.png", "medication_distribution_by_stage.png",
        "updrs_by_medication.png", "updrs_by_disease_stage.png",
        "updrs_over_years.png", "updrs_by_gender.png",
        "updrs_vs_age.png", "tremor_vs_age.png",
        "speech_difficulty_by_gender.png"
    ]
    for f in expected:
        assert f in files, f"{f} missing!"
