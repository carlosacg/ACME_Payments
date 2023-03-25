from django.contrib import messages


def uw_add_alert(request, text, type_message="success"):
    """
    This function allow to generate session mesagges
    :param request:
    :param text:
    :param type_message:
    :return:
    """
    types_message = {
        "debug": messages.DEBUG,
        "info": messages.INFO,
        "success": messages.SUCCESS,
        "warning": messages.WARNING,
        "error": messages.ERROR,
        "danger": messages.ERROR,
    }

    if type_message in types_message:
        type_message = types_message[type_message]
    else:
        type_message = types_message["success"]

    messages.add_message(request, type_message, text, extra_tags="alert")


