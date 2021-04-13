from typing import List, Dict, Callable, Tuple

SlotValidationResult = Tuple[bool, bool, str, Dict]


class Validator:
    def __init__(self):
        self.filled = False
        self.partially_filled = True
        self.trigger = ""
        self.parameters = {}

    def validate_finite_values_entity(self, **kwargs) -> SlotValidationResult:
        pick_first = kwargs["pick_first"]
        values = kwargs["values"]
        supported_values = kwargs["supported_values"]
        key = kwargs["key"]
        entity_type = kwargs["type"]

        if len(supported_values) == 0 or len(values) == 0:
            self.trigger = kwargs["invalid_trigger"]
            return self.get_response()

        elif pick_first:
            if (
                values[0]["entity_type"] == entity_type
                and values[0]["value"] in supported_values
            ):
                self.filled = True
                self.partially_filled = False
                self.parameters[key] = values[0]["value"]
            else:
                self.trigger = kwargs["invalid_trigger"]
            return self.get_response()

        else:
            flag = True
            for entity in values:
                if (
                    entity["entity_type"] not in entity_type
                    or entity["value"] not in supported_values
                ):
                    flag = False
                else:
                    if self.parameters.get(key) == None:
                        self.parameters[key] = []
                    self.parameters[key].append(entity["value"].upper())

            self.filled = flag
            self.partially_filled = not flag
            if self.partially_filled:
                self.trigger = kwargs["invalid_trigger"]

            return self.get_response()

    def get_response(self):
        return (self.filled, self.partially_filled, self.trigger, self.parameters)

    def format_response(self, response):
        {
            "filled": response[0],
            "partially_filled": response[1],
            "trigger": response[2],
            "parameters": response[3],
        }