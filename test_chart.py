import possible_rates_chart
import unittest.mock as mock

def test_numbers_output(capsys):
    with mock.patch('builtins.input', side_effect=["10003.20.001", "45", '250000']):
        possible_rates_chart.print_rates_chart()
        
        captured = capsys.readouterr()
        outputs = captured.out


        assert "| 10003.20.001 |     45 |          $0.00 | 4.875% |" in outputs
        assert "| 10003.20.001 |     45 |      $1,557.50 | 4.750% |" in outputs
        assert "| 10003.20.001 |     45 |     $-5,025.00 | 5.990% |" in outputs


def test_border_output(capsys):
    with mock.patch('builtins.input', side_effect=["10003.20.001", "45", '250000']):
        possible_rates_chart.print_rates_chart()
        
        captured = capsys.readouterr()
        outputs = captured.out

        assert "|--------------|--------|----------------|--------|" in outputs
