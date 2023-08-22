from base import Base

class Test(Base):
    def initialize(self):
        print("initializing")

    def update(self):
        print("updating")


Test().run()