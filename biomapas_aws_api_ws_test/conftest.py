from biomapas_aws_api_ws_test.testing_manager import TestingManager


def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """
    TestingManager.bootstrap()
    TestingManager.prepare_infrastructure()


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    pass


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    TestingManager.destroy_infrastructure()


def pytest_unconfigure(config):
    """
    Called before test process is exited.
    """
    pass