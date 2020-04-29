from functools import partial

from rest_framework import viewsets, permissions

from buildingmgmt.serializers import ProjectSerializer, ProposalSerializer
from buildingmgmt.models import Project, Proposal

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-deadline')
    serializer_class = partial(ProjectSerializer, context = {'request': None})
    permissions_classes = [ permissions.IsAuthenticated ]

# 

class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    permissions_classes = [ permissions.IsAuthenticated ]
