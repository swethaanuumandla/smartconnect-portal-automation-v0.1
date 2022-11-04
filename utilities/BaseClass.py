import pytest


@pytest.mark.usefixtures ( "setup" )
class BaseClass:
    pass
    print("baseclass")
