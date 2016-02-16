from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
trip = Table('trip', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('origin', String(length=10)),
    Column('destination', String(length=10)),
    Column('timeLeaving', DateTime),
    Column('user_id', Integer),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('email', VARCHAR(length=120)),
    Column('fullname', VARCHAR(length=64)),
    Column('age', INTEGER),
    Column('carType', VARCHAR(length=64)),
    Column('origin', VARCHAR(length=10)),
    Column('destination', VARCHAR(length=10)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['trip'].create()
    pre_meta.tables['user'].columns['destination'].drop()
    pre_meta.tables['user'].columns['origin'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['trip'].drop()
    pre_meta.tables['user'].columns['destination'].create()
    pre_meta.tables['user'].columns['origin'].create()
