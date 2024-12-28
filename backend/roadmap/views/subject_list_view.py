from rest_framework.generics import ListAPIView
from ..models import Subject
from ..serializers import SubjectsSerializer


class SubjectListView(ListAPIView):
    """
    Handles operations related to the Subject list view.

    This class is a Django REST framework ListAPIView that provides functionality
    to retrieve a list of all Subject objects. It utilizes a specified serializer
    class to format the retrieved data.

    Attributes:
        queryset: A QuerySet of all Subject objects, targeting the Subject model.
        serializer_class: The class used to serialize the Subject data.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectsSerializer
