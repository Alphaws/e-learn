from rest_framework.generics import RetrieveAPIView, ListAPIView


class SubjectRoadmapsView(ListAPIView):

    def get_queryset(self):
        """
        Csak a megadott tantárgyhoz kapcsolódó blogbejegyzéseket listázza.
        """

