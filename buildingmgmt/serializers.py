from rest_framework import serializers

# Models to serialize
from buildingmgmt.models import Project
from buildingmgmt.models import Proposal

class RelativeHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    def __init__(self, *args, **kwargs):
        if not 'context' in kwargs:
            kwargs['context'] = {}
        if not 'request' in kwargs['context']:
            kwargs['context']['request'] = {}
        kwargs['context']['request'] = None
        super().__init__(*args, **kwargs)

class ProposalSerializer(RelativeHyperlinkedModelSerializer):
    class Meta:
        model = Proposal
        fields = [ 'id', 'project', 'contractor', 'contractor_email', 'contractor_response', 'offer', 'is_within_budget', 'state']

class ProjectSerializer(RelativeHyperlinkedModelSerializer):
    proposals = ProposalSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = [ 'id', 'title', 'description', 'deadline', 'budget', 'proposals']
