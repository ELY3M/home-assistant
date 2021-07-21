"""Support for tracking the moon phases with more details!   ELY M."""
from astral import moon
import voluptuous as vol
import logging

from homeassistant.components.sensor import PLATFORM_SCHEMA, SensorEntity
from homeassistant.const import CONF_NAME
import homeassistant.helpers.config_validation as cv
import homeassistant.util.dt as dt_util

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = "Moon"

STATE_MOON0 = "moon0"
STATE_MOON1 = "moon1"
STATE_MOON2 = "moon2"
STATE_MOON3 = "moon3"
STATE_MOON4 = "moon4"
STATE_MOON5 = "moon5"
STATE_MOON6 = "moon6"
STATE_MOON7 = "moon7"
STATE_MOON8 = "moon8"
STATE_MOON9 = "moon9"
STATE_MOON10 = "moon10"
STATE_MOON11 = "moon11"
STATE_MOON12 = "moon12"
STATE_MOON13 = "moon13"
STATE_MOON14 = "moon14"
STATE_MOON15 = "moon15"
STATE_MOON16 = "moon16"
STATE_MOON17 = "moon17"
STATE_MOON18 = "moon18"
STATE_MOON19 = "moon19"
STATE_MOON20 = "moon20"
STATE_MOON21 = "moon21"
STATE_MOON22 = "moon22"
STATE_MOON23 = "moon23"
STATE_MOON24 = "moon24"
STATE_MOON25 = "moon25"
STATE_MOON26 = "moon26"
STATE_MOON27 = "moon27"
STATE_MOON28 = "moon28"
STATE_MOON29 = "moon29"

MOON_NAME = {
    STATE_MOON0: "New Moon", 
    STATE_MOON1: "Waxing Crescent",  
    STATE_MOON2: "Waxing Crescent",   
    STATE_MOON3: "Waxing Crescent",  
    STATE_MOON4: "Waxing Crescent",   
    STATE_MOON5: "Waxing Crescent",   
    STATE_MOON6: "Waxing Crescent",   
    STATE_MOON7: "First Quarter",   
    STATE_MOON8: "Waxing Gibbous",   
    STATE_MOON9: "Waxing Gibbous",   
    STATE_MOON10: "Waxing Gibbous",
    STATE_MOON11: "Waxing Gibbous",
    STATE_MOON12: "Waxing Gibbous",
    STATE_MOON13: "Waxing Gibbous",
    STATE_MOON14: "Waxing Gibbous",
    STATE_MOON15: "Full Moon",
    STATE_MOON16: "Waning Gibbous",
    STATE_MOON17: "Waning Gibbous",
    STATE_MOON18: "Waning Gibbous",
    STATE_MOON19: "Waning Gibbous",
    STATE_MOON20: "Waning Gibbous",
    STATE_MOON21: "Waning Gibbous",
    STATE_MOON22: "Waning Gibbous",
    STATE_MOON23: "Last Quarter",
    STATE_MOON24: "Waning Crescent",
    STATE_MOON25: "Waning Crescent",
    STATE_MOON26: "Waning Crescent",
    STATE_MOON27: "Waning Crescent",
    STATE_MOON28: "Waning Crescent",
    STATE_MOON29: "Waning Crescent",
}


MOON_ICONS = {
    STATE_MOON0: "mdi:moon-new", 
    STATE_MOON1: "mdi:moon-waxing-crescent",  
    STATE_MOON2: "mdi:moon-waxing-crescent",   
    STATE_MOON3: "mdi:moon-waxing-crescent",  
    STATE_MOON4: "mdi:moon-waxing-crescent",   
    STATE_MOON5: "mdi:moon-waxing-crescent",   
    STATE_MOON6: "mdi:moon-waxing-crescent",   
    STATE_MOON7: "mdi:moon-first-quarter",   
    STATE_MOON8: "mdi:moon-waxing-gibbous",   
    STATE_MOON9: "mdi:moon-waxing-gibbous",   
    STATE_MOON10: "mdi:moon-waxing-gibbous",
    STATE_MOON11: "mdi:moon-waxing-gibbous",
    STATE_MOON12: "mdi:moon-waxing-gibbous",
    STATE_MOON13: "mdi:moon-waxing-gibbous",
    STATE_MOON14: "mdi:moon-waxing-gibbous",
    STATE_MOON15: "mdi:moon-full",
    STATE_MOON16: "mdi:moon-waning-gibbous",
    STATE_MOON17: "mdi:moon-waning-gibbous",
    STATE_MOON18: "mdi:moon-waning-gibbous",
    STATE_MOON19: "mdi:moon-waning-gibbous",
    STATE_MOON20: "mdi:moon-waning-gibbous",
    STATE_MOON21: "mdi:moon-waning-gibbous",
    STATE_MOON22: "mdi:moon-waning-gibbous",
    STATE_MOON23: "mdi:moon-last-quarter",
    STATE_MOON24: "mdi:moon-waning-crescent",
    STATE_MOON25: "mdi:moon-waning-crescent",
    STATE_MOON26: "mdi:moon-waning-crescent",
    STATE_MOON27: "mdi:moon-waning-crescent",
    STATE_MOON28: "mdi:moon-waning-crescent",
    STATE_MOON29: "mdi:moon-waning-crescent",
}

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string}
)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Moon sensor."""
    name = config.get(CONF_NAME)

    async_add_entities([MoonSensor(name)], True)


class MoonSensor(SensorEntity):
    """Representation of a Moon sensor."""

    def __init__(self, name):
        """Initialize the moon sensor."""
        self._name = name
        self._state = None

    @property
    def name(self):
        """Return the name of the entity."""
        return self._name

    @property
    def device_class(self):
        """Return the device class of the entity."""
        return "moon__phase"

    @property
    def state(self):
        """Return the state of the device."""
        if self._state <= 0:
            return STATE_MOON0
        if self._state <= 1:
            return STATE_MOON1
        if self._state <= 2:
            return STATE_MOON2
        if self._state <= 3:
            return STATE_MOON3
        if self._state <= 4:
            return STATE_MOON4			
        if self._state <= 5:
            return STATE_MOON5				
        if self._state <= 6:
            return STATE_MOON6				
        if self._state <= 7:
            return STATE_MOON7				
        if self._state <= 8:
            return STATE_MOON8	
        if self._state <= 9:
            return STATE_MOON9	
        if self._state <= 10:
            return STATE_MOON10
        if self._state <= 11:
            return STATE_MOON11
        if self._state <= 12:
            return STATE_MOON12
        if self._state <= 13:
            return STATE_MOON13
        if self._state <= 14:
            return STATE_MOON14
        if self._state <= 15:
            return STATE_MOON15
        if self._state <= 16:
            return STATE_MOON16
        if self._state <= 17:
            return STATE_MOON17
        if self._state <= 18:
            return STATE_MOON18
        if self._state <= 19:
            return STATE_MOON19
        if self._state <= 20:
            return STATE_MOON20
        if self._state <= 21:
            return STATE_MOON21		
        if self._state <= 22:
            return STATE_MOON22
        if self._state <= 23:
            return STATE_MOON23		
        if self._state <= 24:
            return STATE_MOON24
        if self._state <= 25:
            return STATE_MOON25
        if self._state <= 26:
            return STATE_MOON26
        if self._state <= 27:
            return STATE_MOON27
        if self._state <= 28:
            return STATE_MOON28					
        if self._state <= 29:
            return STATE_MOON29
        return STATE_MOON10

    @property
    def moonphasename(self):
        """Moon Phase Name to use"""
        return MOON_NAME.get(self.state)
		
    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return MOON_ICONS.get(self.state)

    async def async_update(self):
        """Get the time and updates the states."""
        today = dt_util.as_local(dt_util.utcnow()).date()
        self._state = moon.phase(today)
