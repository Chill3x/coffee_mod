from enum import Enum
class CoffeeCommands(Enum):
    START_MACHINE = 'AN:01'
    STOP_MACHINE = 'AN:02'
    TEST_DISPLAY = 'AN:03'
    MAKE_PRODUCT_1 = 'FA:01'
    MAKE_PRODUCT_2 = 'FA:02'
    MAKE_PRODUCT_3 = 'FA:03'
    MAKE_PRODUCT_4 = 'FA:04'
    MAKE_PRODUCT_5 = 'FA:05'
    MAKE_PRODUCT_6 = 'FA:06'
    MAKE_PRODUCT_7 = 'FA:07'
    MAKE_HOT_WATER = 'FA:08'
    MAKE_STEAM = 'FA:09'
    FLUSHING = 'FA:0B'
    PUMP_COFFEE_ON = 'FN:01'
    PUMP_COFFEE_OFF = 'FN:02'
    COFFEE_HEATING_ON = 'FN:03'
    COFFEE_HEATING_OFF = 'FN:04'
    STEAM_HEATING_ON = 'FN:05'
    STEAM_HEATING_OFF = 'FN:06'
    GRINDER_LEFT_ON = 'FN:07'
    GRINDER_LEFT_OFF = 'FN:08'
    GRINDER_RIGHT_ON = 'FN:09'
    GRINDER_RIGHT_OFF = 'FN:0A'
    PUMP_STEAM_ON = 'FN:0B'
    PUMP_STEAM_OFF = 'FN:0C'
    INIT_BREWGROUP = 'FN:0D'
    BREWGROUP_IN_GRINDING_POS = 'FN:0F'
    BREWGROUP_IN_BREWING_POS = 'FN:13'
    DRAINAGE_VALVE_ON = 'FN:1D'
    DRAINAGE_VALVE_OFF = 'FN:1E'
    EMPTY_STEAM_VALVE_ON = 'FN:24'
    EMPTY_STEAM_VALVE_OFF = 'FN:25'
    STEAM_VALVE_ON = 'FN:26'
    STEAM_VALVE_OFF = 'FN:27'
    CAPPUCCINO_VALVE_ON = 'FN:28'
    CAPPUCCINO_VALVE_OFF = 'FN:29'
    BREWGROUP_PUT_TRESTER_OFF = 'FN:0E'
    TYPE_OF_MACHINE = 'TY:'
    