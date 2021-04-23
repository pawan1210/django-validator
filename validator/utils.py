class Validator:
    def __init__(self):
        self.filled = False
        self.partially_filled = True
        self.trigger = ""
        self.parameters = {}

    def validate_finite_values_entity(self, **kwargs):
        pick_first = kwargs["pick_first"]
        values = kwargs["values"]
        supported_values = kwargs["supported_values"]
        key = kwargs["key"]
        entity_type = kwargs["type"]

        if len(supported_values) == 0 or len(values) == 0:
            self.partially_filled = False
            self.trigger = kwargs["invalid_trigger"]
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

            if pick_first:
                self.parameters = {}
                if (
                    values[0]["entity_type"] == entity_type
                    and values[0]["value"] in supported_values
                ):
                    self.parameters[key] = values[0]["value"]

        return self.get_response()

    def validate_numeric_entity(self, **kwargs):
        pick_first = kwargs["pick_first"]
        values = kwargs["values"]
        key = kwargs["key"]
        constraint = kwargs["constraint"]
        entity_type = kwargs["type"]
        conjunction, parsed_constraints = self.parse_constraint(constraint)

        if len(values) == 0:
            self.partially_filled = False
            self.trigger = kwargs["invalid_trigger"]

        else:
            flag = True
            for entity in values:
                result = self.compare_with_conjunction(
                    entity["value"], parsed_constraints, conjunction
                )
                if result:
                    if self.parameters.get(key) == None:
                        self.parameters[key] = []
                    self.parameters[key].append(entity["value"])
                else:
                    flag = False

            self.filled = flag
            self.partially_filled = not flag

            if self.partially_filled:
                self.trigger = kwargs["invalid_trigger"]

            if pick_first:
                self.parameters = {}
                if self.compare_with_conjunction(
                    values[0]["value"], parsed_constraints, conjunction
                ):
                    self.parameters[key] = values[0]["value"]

        return self.get_response()

    def get_response(self):
        return (self.filled, self.partially_filled, self.trigger, self.parameters)

    def format_response(self, response):
        return {
            "filled": response[0],
            "partially_filled": response[1],
            "trigger": response[2],
            "parameters": response[3],
        }

    def parse_constraint(self, constraint):
        constraints = []
        conjunction = None
        if "and" in constraint:
            conjunction = "and"
            constraints = constraint.split("and")
        elif "or" in constraint:
            conjunction = "or"
            constraints = constraint.split("or")
        else:
            constraints.append(constraint)

        return conjunction, self.parse_single_constraint(constraints)

    def parse_single_constraint(self, constraints):
        parsed_constraints = []
        for constraint in constraints:
            constraint = constraint.strip()
            operator = None
            if ">=" in constraint:
                operator = ">="
            elif "<=" in constraint:
                operator = "<="
            elif ">" in constraint:
                operator = ">"
            elif "<" in constraint:
                operator = "<"
            elif "==" in constraint:
                operator = "=="
            parsed_constraints.append(
                {"operator": operator, "value": int(constraint.split(operator)[1])}
            )

        return parsed_constraints

    def compare_value(self, value, constraint):
        operator = constraint["operator"]
        if operator == ">=":
            return value >= constraint["value"]
        elif operator == "<=":
            return value <= constraint["value"]
        elif operator == ">":
            return value > constraint["value"]
        elif operator == "<":
            return value < constraint["value"]
        elif operator == "==":
            return value == constraint["value"]

    def compare_with_conjunction(self, value, constraints, conjunction):
        if conjunction == "and":
            left = self.compare_value(value, constraints[0])
            right = self.compare_value(value, constraints[1])
            return left and right
        elif conjunction == "or":
            left = self.compare_value(value, constraints[0])
            right = self.compare_value(value, constraints[1])
            return left or right
        else:
            return self.compare_value(value, constraints[0])
