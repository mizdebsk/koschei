from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.engine.url import URL

db_settings = {'drivername': 'postgres',
               'host': 'localhost',
               'port': '5432',
               'username': 'msimacek',
               'password': 'fedorawtf',
               'database': 'fedora-ci'}

Base = declarative_base()

engine = create_engine(URL(**db_settings), echo=False)

Session = sessionmaker(bind=engine)


class Package(Base):
    __tablename__ = 'package'

    id = Column(Integer, primary_key=True)
    name = Column('name', String, nullable=False, unique=True)
    priority = Column('priority', Integer, nullable=False, default=0)
    builds = relationship('Build', backref='package')

    plugin_data = relationship('PluginData', backref='package', lazy='dynamic')

    def __repr__(self):
        return '{0.id} (name={0.name}, priority={0.priority})'.format(self)

class Build(Base):
    __tablename__ = 'build'

    id = Column(Integer, primary_key=True)
    package_id = Column(Integer, ForeignKey('package.id'))
    state = Column(Integer, nullable=False, default=0)
    task_id = Column(Integer)

    SCHEDULED = 0
    RUNNING = 2
    COMPLETE = 3
    CANCELED = 4
    FAILED = 5

    UNFINISHED_STATES = [SCHEDULED, RUNNING]
    FINISHED_STATES = [COMPLETE, FAILED, CANCELED]
    STATES = UNFINISHED_STATES + FINISHED_STATES

    def __repr__(self):
        return '{0.id} (name={0.package.name}, state={0.state})'.format(self)

class PluginData(Base):
    __tablename__ = 'plugin_data'

    id = Column(Integer, primary_key=True)
    package_id = Column(Integer, ForeignKey('package.id'))
    plugin_name = Column(String, nullable=False)
    key = Column(String, nullable=False)
    value = Column(String)

