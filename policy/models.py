from django.db import models


class PolicyAcknowledgment(models.Model):
    """An auditable record of a user's agreement to a policy version."""

    user_name = models.CharField(max_length=100)
    policy_version = models.CharField(max_length=20)
    acknowledged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user_name} acknowledged v{self.policy_version} "
            f"at {self.acknowledged_at}"
        )
