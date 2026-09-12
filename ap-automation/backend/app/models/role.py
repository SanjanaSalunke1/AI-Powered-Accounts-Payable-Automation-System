from enum import Enum


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    FINANCE = "FINANCE"
    REVIEWER = "REVIEWER"
    APPROVER = "APPROVER"