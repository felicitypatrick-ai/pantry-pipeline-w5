"""Northside Food Pantry: release check, run right after each deploy (course sample code)."""
import os
import sys

release, environment = sys.argv[1], sys.argv[2]
sys.path.insert(0, release)  # import the deployed files, not the repository's

from settings import SATURDAY_CAPACITY
from slots import slots_left
from waitlist import waitlist_position

print(f"Release check: {environment}")
print(open(os.path.join(release, "RELEASE.txt")).read().strip())
print("Saturday capacity:", SATURDAY_CAPACITY)
print("Open slots with 18 booked:", slots_left(SATURDAY_CAPACITY, 18))
print("Place in line of the first family on the waitlist:", waitlist_position(["Garcia", "Nguyen"], "Garcia"))
print("Release check passed.")
