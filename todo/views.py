from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ToDoSerializer
from .models import ToDo
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from datetime import datetime, date


class ToDoViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
        user = self.request.user
        todos = ToDo.objects.filter(user=user)

        # optional query params
        # e.g. /api/todos/?id=1
        #      /api/todos/?overdue=true
        #      /api/todos/?completed=false
        todo_id = self.request.query_params.get('id')
        overdue = self.request.query_params.get('overdue')
        completed = self.request.query_params.get('completed')

        if todo_id:
            todos = todos.filter(id=todo_id)

        if overdue == 'true':
            todos = todos.filter(end_date__lt=date.today())
        elif overdue == 'false':
            todos = todos.filter(end_date__gte=date.today())

        if completed == 'true':
            todos = todos.filter(completed=1)
        elif completed == 'false':
            todos = todos.filter(completed=0)

        return todos

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, completed=0)

    # /api/todos/<pk>/update_todo/
    # include fields in request body
    @action(methods=['POST'], detail=True)
    def update_todo(self, request, pk):        
        try:
            todo = ToDo.objects.get(pk=pk)
            todo.name = request.data['name']
            todo.description = request.data['description']
            todo.start_date = request.data['start_date']
            todo.end_date = request.data['end_date']

            todo.save()

            serializer = ToDoSerializer(todo, many=False)
            response = serializer.data
            status_code = status.HTTP_200_OK

        except:
            response = {'failed': 'could not update todo'}
            status_code = status.HTTP_400_BAD_REQUEST

        return Response(response, status=status_code)

    # /api/todos/<pk>/mark_completed/
    # No request body. Sets completed to 1 (true) and sets date completed to current date
    @action(methods=['POST'], detail=True)
    def mark_completed(self, request, pk):
        try:
            todo = ToDo.objects.get(pk=pk)
            todo.completed = 1
            todo.date_completed = datetime.now().strftime('%Y-%m-%d')

            todo.save()

            serializer = ToDoSerializer(todo, many=False)
            response = serializer.data
            status_code = status.HTTP_200_OK

        except:
            response = {'failed': 'could not complete todo'}
            status_code = status.HTTP_400_BAD_REQUEST

        return Response(response, status=status_code)

