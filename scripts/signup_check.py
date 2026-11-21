"""Northside Food Pantry: sign-up check (course sample code).
Checks the open slots and the waitlist against the pantry's rules.
It waits 20 seconds on purpose: it stands in for a slow check on a real project."""
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.slots import can_book, slots_left
from app.waitlist import waitlist_position

WAIT_SECONDS = 20


def check_slots():
    """Open slots are capacity minus booked; a family can book while a slot is open."""
    for capacity in range(1, 31):
        for booked in range(0, capacity + 1):
            if slots_left(capacity, booked) != capacity - booked:
                return f"capacity {capacity} with {booked} booked shows {slots_left(capacity, booked)} open slots"
            if can_book(capacity, booked) != (booked < capacity):
                return f"capacity {capacity} with {booked} booked gives the wrong booking answer"
    return None


def check_waitlist():
    """The pantry counts from 1: the first family is number 1."""
    families = ["Garcia", "Nguyen", "Okafor", "Patel"]
    for place, family in enumerate(families, 1):
        if waitlist_position(families, family) != place:
            return f"family {place} on the waitlist is told number {waitlist_position(families, family)}"
    return None


PARTS = {"slots": check_slots, "waitlist": check_waitlist}
part = sys.argv[1] if len(sys.argv) > 1 else ""
if part not in PARTS:
    print(f"Unknown part: {part}. Use slots or waitlist.")
    sys.exit(2)
time.sleep(WAIT_SECONDS)
problem = PARTS[part]()
if problem:
    print(f"Sign-up check failed: {problem}")
    sys.exit(1)
print(f"Sign-up check passed: {part}")
