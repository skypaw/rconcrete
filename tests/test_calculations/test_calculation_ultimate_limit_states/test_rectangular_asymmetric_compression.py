import pytest
from src.calculations.calculation_ultimate_limit_states import AsymmetricCompression


def helper_calculation(bending_moment: float, normal_force: float) -> dict:
    calculation_data = {"height": 0.6, "width": 0.3, "top_reinforcement_distance": 0.05,
                        "bottom_reinforcement_distance": 0.05, "bending_moment": bending_moment,
                        "normal_force": normal_force, "factor_eta": 1.0, "factor_lambda": 0.8,
                        "concrete_plasticity": 30, "steel_plasticity": 500}
    return calculation_data


@pytest.mark.parametrize("input_data, expected_reinforcement", [(helper_calculation(5, 10), (0.21984, 1.8)),
                                                                (helper_calculation(100, 100), (3.102643, 1.8)),
                                                                (helper_calculation(1000, 500), (17.95217, 1.8)),
                                                                (helper_calculation(1000, 750), (29.879164, 12.74813)),
                                                                (helper_calculation(3500, 500), (4.025, 21.79357)),
                                                                (helper_calculation(3500, 350), (4.025, 12.94635)),
                                                                (helper_calculation(5000, 300), (5.75, 26.74230)),
                                                                (helper_calculation(5000, 250), (5.75, 24.60759)),
                                                                (helper_calculation(5000, 225), (4.578443, 23.49285)),
                                                                (helper_calculation(5000, 100), (12.95305, 18.66734)),
                                                                (helper_calculation(5000, 25), (15.58093, 17.0095)),
                                                                (helper_calculation(5000, 0), (16.32650, 16.32650))])
def test_rectangular_asymmetric_compression(input_data, expected_reinforcement):
    reinforcement = AsymmetricCompression(input_data).calculate()

    assert reinforcement == pytest.approx(expected_reinforcement)
