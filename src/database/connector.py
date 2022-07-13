from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta
import json

class Manager:
    base = declarative_base()
    session = None

    def create_engine(self):
        engine = create_engine('sqlite:///message.db?check_same_thread=False', echo=False)
        self.base.metadata.create_all(engine)

        return engine

    def get_session(self, engine):
        if self.session == None:
            _session = sessionmaker(bind=engine)
            session = _session()

        return session

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None

            return fields

        return json.JSONEncoder.default(self, obj)
