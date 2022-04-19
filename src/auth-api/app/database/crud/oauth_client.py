"""
    OAuth client CRUD utils for the database.
"""

# Libraries.
import secrets
from sqlalchemy.orm import Session

# Services.
from app.database.models.oauth_client import OAuthClient


def generate_secret() -> str:
    """ Returns generate client secret. """
    return secrets.token_urlsafe(32)


def get_by_id(db: Session, client_id: int) -> OAuthClient:
    """ Returns client by it`s ID. """
    return db.query(OAuthClient).filter(OAuthClient.id == client_id).first()


def expire(db: Session, client: OAuthClient):
    """ Regenerates client secret. """
    client.secret = generate_secret()
    db.commit()

def create(db: Session, owner_id: int) -> OAuthClient:
    """Creates OAuth client"""

    # Create new OAuth client.
    oauth_client_secret = generate_secret()
    oauth_client = OAuthClient(secret=oauth_client_secret, owner_id=owner_id)

    # Apply OAuth client in database.
    db.add(oauth_client)
    db.commit()
    db.refresh(oauth_client)

    return oauth_client