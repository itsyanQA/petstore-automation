from scheme_custom.ApiResponseMetaData import ApiResponseMetaData


def is_order_placed(response: ApiResponseMetaData):
    """Return false if status code equals to 404, true otherwise, used for slow endpoints."""
    if response.status_code == 404:
        return False
    else:
        return True
