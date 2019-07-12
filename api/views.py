from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import ToDos, ToDoSerializer

"""
The ContactsView will contain the logic on how to:
 GET, POST, PUT or delete the contacts
"""


class ToDosView(APIView):
    def get(self, request, toDosItem_id=None):

        if toDosItem_id is not None:
            peo = ToDo.objects.get(id=toDosItem_id)
            serializer = ToDoSerializer(peo, many=False)
            return Response(serializer.data)
        else:
            peo = ToDo.objects.all()
            serializer = ToDoSerializer(toDos, many=True)
            return Response(serializer.data)

    def post(self, request):

        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, toDosItem_id):

        toDo = ToDo.objects.get(id=toDosItem_id)
        toDo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
