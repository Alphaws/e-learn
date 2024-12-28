from rest_framework.generics import RetrieveAPIView

from roadmap.models import Subject
from roadmap.serializers import SubjectsSerializer


class SubjectRetrieveView(RetrieveAPIView):
    serializer_class = SubjectsSerializer
    queryset = Subject.objects.all()
    lookup_field = 'slug'