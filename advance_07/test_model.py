from unittest import mock
import pytest

from model import predict_message_mood


@pytest.mark.parametrize(
    "bad_thresholds,good_thresholds,pred,expected_str",
    [
        (0., 0., 0., "норм"),
        (0.5, 0.5, 0.5, "норм"),
        (1., 1., 1., "норм"),
        (0., 1., 0.5, "норм"),
        (0.3, 0.6, 0.3, "норм"),
        (0.3, 0.6, 0.6, "норм"),
        (0.3, 0.6, 0.2, "неуд"),
        (0.3, 0.6, 0.8, "отл"),
    ]
)
def test_predict_message_mood(bad_thresholds, good_thresholds, pred, expected_str):
    with mock.patch("model.SomeModel") as mock_model:
        instance = mock_model.return_value
        instance.predict.return_value = pred

        assert predict_message_mood(None, mock_model(), bad_thresholds, good_thresholds) \
            == expected_str


@pytest.mark.parametrize(
    "bad_thresholds,good_thresholds,error_message", [
        (-1., 0., "bad_thresholds=-1.0 must in the range from 0 to 1"),
        (2., 0., "bad_thresholds=2.0 must in the range from 0 to 1"),
        (0., -1, "good_thresholds=-1 must in the range from 0 to 1"),
        (0., 2, "good_thresholds=2 must in the range from 0 to 1"),
        (0.6, 0.3, "good_thresholds=0.3 must be more than bad_thresholds=0.6")
    ]
)
def test_predict_message_mood_raise_value_error(bad_thresholds, good_thresholds, error_message):
    with pytest.raises(ValueError, match=error_message):
        predict_message_mood(None, None, bad_thresholds, good_thresholds)
