from component.button import ButtonElement, ButtonList
from component.modal import ConfirmationModal

clickable_list:list = [ButtonList,ButtonElement, ConfirmationModal]

def is_instance_of_class(variable, class_list=clickable_list):
    """
    Check if a variable is an instance of any class in the class_list.

    Args:
        variable: The variable to be checked.
        class_list: A list of class names or classes.

    Returns:
        True if the variable is an instance of any class in the class_list, False otherwise.
    """
    for cls in class_list:
        if isinstance(variable, cls):
            return True
    return False