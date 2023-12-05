"""
Mechanism for blocking rooms during the reservation period.
"""
from hotel_management import models as hotel_models


class RoomLocking:
    not_valid_status = ['NotAvailable', 'Reserved', 'Occupied']

    def is_available(self, room):
        if room.status in self.not_valid_status:
            return False
        self.set_as_reserved(room=room)

    @staticmethod
    def set_as_reserved(room):
        room.status = 'Reserved'
        room.save()
        return room
