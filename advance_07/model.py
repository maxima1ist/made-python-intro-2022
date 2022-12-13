import random


class SomeModel:
    def predict(self, message: str) -> float:
        pass


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    if 0 > bad_thresholds or bad_thresholds > 1:
        raise ValueError(f"{bad_thresholds=} must in the range from 0 to 1")

    if 0 > good_thresholds or good_thresholds > 1:
        raise ValueError(f"{good_thresholds=} must in the range from 0 to 1")

    if bad_thresholds > good_thresholds:
        raise ValueError(
            f"{good_thresholds=} must be more than {bad_thresholds=}")

    pred = model.predict(message)
    if pred < bad_thresholds:
        return "неуд"
    if pred > good_thresholds:
        return "отл"
    return "норм"
