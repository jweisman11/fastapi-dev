from fastapi import Header


def custom_headers(
    X_API_Key: str | None = Header(default=None),
    X_Proxied_Entity: str | None = Header(default=None),
    X_Proxied_Issuer: str | None = Header(default=None),
) -> dict:
    """
    Custom headers for all routes
    """
    return {
        "X-API-Key": X_API_Key,
        "X-Proxied-Entity": X_Proxied_Entity,
        "X-Proxied-Issuer": X_Proxied_Issuer,
    }
