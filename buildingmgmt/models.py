from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    deadline = models.DateField()
    budget = models.IntegerField()

class Proposal(models.Model):
    PROPOSAL_STATES = (
        ('OPEN', 'Open - A request for a quote has been sent'),
        ('VALIDATING', 'Validating - A proposal/quote has been received'),
        ('APPROVED', 'Approved - A proposal/quote has been aproved and will be considered'),
        ('CHOSEN', 'Chosen - The given projects actually chosen proposal'),
        ('CLOSED', 'Closed - The project proposal has been closed'),
    )
    project  = models.ForeignKey(Project, related_name='proposals', on_delete=models.CASCADE)

    state = models.CharField(max_length=100, choices=PROPOSAL_STATES, default="OPEN")

    contractor = models.CharField(max_length=100, blank=False)
    contractor_email = models.CharField(max_length=100, blank=False)
    contractor_response = models.TextField(blank=True)
    offer = models.IntegerField(default=0)

    class Meta:
        ordering = []

    def is_within_budget(self):
        return self.project.budget >= self.offer
