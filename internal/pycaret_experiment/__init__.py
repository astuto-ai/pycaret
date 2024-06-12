class TimeSeriesExperiment:
    def __init__(self) -> None:
        msg = (
            "\nTimeSeriesExperiment class has been deprecated. "
            "Please import the following instead.\n"
            ">>> from onelens.onelens_pycaret.time_series import TSForecastingExperiment"
        )
        raise DeprecationWarning(msg)
