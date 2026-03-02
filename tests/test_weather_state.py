"""Test module for WeatherStateMachine."""

from weather_state import WeatherState, WeatherStateMachine


class TestWeatherState:
    """Tests for WeatherState enum."""

    def test_state_values(self):
        """Test that state enum has correct values."""
        assert WeatherState.ERROR.value == 0
        assert WeatherState.FETCHING.value == 1
        assert WeatherState.INIT.value == 2
        assert WeatherState.SUCCESS.value == 3


class TestWeatherStateMachine:
    """Tests for WeatherStateMachine class."""

    def test_initial_state(self):
        """Test that state machine initializes in ERROR state."""
        machine = WeatherStateMachine()
        assert machine.state == WeatherState.ERROR

    def test_data_received_from_fetching(self):
        """Test transition from FETCHING to SUCCESS on data_received."""
        machine = WeatherStateMachine()
        machine._state = WeatherState.FETCHING
        machine.data_received()
        assert machine.state == WeatherState.SUCCESS

    def test_data_received_from_other_states(self):
        """Test that data_received does not change state from non-FETCHING states."""
        machine = WeatherStateMachine()
        machine.data_received()
        assert machine.state == WeatherState.ERROR

    def test_request_from_init(self):
        """Test transition from INIT to FETCHING on request."""
        machine = WeatherStateMachine()
        machine._state = WeatherState.INIT
        machine.request()
        assert machine.state == WeatherState.FETCHING

    def test_request_from_success(self):
        """Test transition from SUCCESS to INIT on request."""
        machine = WeatherStateMachine()
        machine._state = WeatherState.SUCCESS
        machine.request()
        assert machine.state == WeatherState.INIT

    def test_request_from_other_states(self):
        """Test that request does not change state from INIT/SUCCESS."""
        machine = WeatherStateMachine()
        machine.request()
        assert machine.state == WeatherState.ERROR

    def test_retry_from_error(self):
        """Test transition from ERROR to INIT on retry."""
        machine = WeatherStateMachine()
        machine.retry()
        assert machine.state == WeatherState.INIT

    def test_retry_from_other_states(self):
        """Test that retry does not change state from non-ERROR states."""
        machine = WeatherStateMachine()
        machine._state = WeatherState.INIT
        machine.retry()
        assert machine.state == WeatherState.INIT

    def test_timeout_from_fetching(self):
        """Test transition from FETCHING to ERROR on timeout."""
        machine = WeatherStateMachine()
        machine._state = WeatherState.FETCHING
        machine.timeout()
        assert machine.state == WeatherState.ERROR

    def test_timeout_from_other_states(self):
        """Test that timeout does not change state from non-FETCHING states."""
        machine = WeatherStateMachine()
        machine.timeout()
        assert machine.state == WeatherState.ERROR

    def test_complete_flow(self):
        """Test a complete flow through the state machine."""
        machine = WeatherStateMachine()
        assert machine.state == WeatherState.ERROR

        machine.retry()
        assert machine.state == WeatherState.INIT

        machine.request()
        assert machine.state == WeatherState.FETCHING

        machine.data_received()
        assert machine.state == WeatherState.SUCCESS

        machine.request()
        assert machine.state == WeatherState.INIT

        machine.request()
        assert machine.state == WeatherState.FETCHING

        machine.timeout()
        assert machine.state == WeatherState.ERROR

        machine.retry()
        assert machine.state == WeatherState.INIT
