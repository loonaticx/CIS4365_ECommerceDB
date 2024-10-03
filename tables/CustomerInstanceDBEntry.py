from base.DatabaseDriver import *
from tables.PersonalInfoInstance import PersonalInfoInstance


# customer will have some redundancy.

class CustomerInstanceDBEntry(Base):
    """
    Skeleton for a db entry in the customer table.

    Will be added into the database upon init
    """

    __tablename__ = "customer"

    id = Column(Integer, primary_key = True, autoincrement = True)
    firstname = Column(String(64))
    lastname = Column(String(64))
    uuid = db.Column(db.String(Config.UUID_TOKEN_LENGTH), unique = True)
    classroom_id = Column(Integer, ForeignKey("classroom.id"))
    classroom = relationship('ClassroomInstanceDBEntry', foreign_keys = [classroom_id])
    children = relationship("ChildInstanceDBEntry", back_populates = "teacher")
    _childids = Column(db.String(512), default = '')

    @property
    def childids(self):
        return [int(x) for x in self._childids.split(';') if x]

    @childids.setter
    def childids(self, value):
        if not value:
            self._childids = ''
        self._childids += '%s;' % value

    def __init__(self, personalInfo: PersonalInfoInstance):
        # NOTE: personal info need not to be stored in the database..? or maybe so... as a record.
        # We should't be dynamically updating personal info then because we want to treat it like a snapshot.
        # Then maybe we should do a blob... but that may be out of scope.
        self.personalInfo = personalInfo
        self.firstname = teacherInstance.firstname
        self.lastname = teacherInstance.lastname
        self.uuid = secrets.token_urlsafe(Config.UUID_TOKEN_LENGTH)

    def __repr__(self):
        return "<TeacherInstanceDBEntry(firstname='%s')>" % (
            self.firstname,
        )
