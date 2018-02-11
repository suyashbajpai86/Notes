from rest_framework import viewsets
from crud.constants import notes
from rest_framework.response import Response


class NotesViewset(viewsets.ViewSet):

    def list(self, request):
        return Response(notes)

    def create(self, request):
        notes.append(request.data)
        return Response("Created successfully")

    def delete(self, pk):
        no = int(self.request.data.get('no'))
        del notes[no-1]
        return Response("deleted successfully")