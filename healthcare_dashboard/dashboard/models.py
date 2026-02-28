from django.db import models

class Claim(models.Model):
    MemberID = models.CharField(max_length=100)
    ClaimID = models.CharField(max_length=100, unique=True)
    ClaimAmount = models.DecimalField(max_digits=10, decimal_places=2)
    ClaimDate = models.DateField()
    ServiceID = models.CharField(max_length=100, blank=True, null=True)
    ProcedureCode = models.CharField(max_length=100, blank=True, null=True)
    Description = models.TextField(blank=True, null=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Claim {self.ClaimID} - Member {self.MemberID}"
    
    class Meta:
        ordering = ['-ClaimDate']
        verbose_name = 'Claim'
        verbose_name_plural = 'Claims'
