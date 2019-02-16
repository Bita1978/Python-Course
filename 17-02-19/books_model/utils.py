class TypeUtils:
    """
    Type utils for type validations
    """

    @staticmethod
    def is_type(var, var_type):
        return type(var) is var_type

    @staticmethod
    def all_of_type(*args, var_type):
        for var in args:
            if type(var) is not var_type:
                return False
        return True


class ErrorMsgUtils:
    """
    Static methods returns a custom error message
    """

    @staticmethod
    def type_error(*args, var_type):
        msg = "Error, "

        if len(args) < 2:
            msg += f"{args[0]} "

        else:
            for arg in args:
                msg += f"{arg}, "

        msg += f"is not {var_type}"
        return msg


    @staticmethod
    def already_exists(var):
        return f'Error, {var} is already exists'

    @staticmethod
    def display_error(error):
        return f"Something went wrong: {error}"

    @staticmethod
    def does_not_exists(table_name, var):
        return f'{table_name} with {var} does not exists'

    @staticmethod
    def no_data_available():
        return 'No data available'