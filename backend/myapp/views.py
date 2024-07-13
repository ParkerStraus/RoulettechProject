from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
import logging

logger = logging.getLogger(__name__)


@api_view(['POST'])
def add_contact(request):
    logger.info('Received a request to add a contact.')
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info('Contact added successfully: %s', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    logger.warning('Failed to add contact: %s', serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_contact(request, pk):
    logger.info('Received a request to delete contact with ID: %d', pk)
    try:
        contact = Contact.objects.get(pk=pk)
        contact.delete()
        logger.info('Contact with ID %d deleted successfully.', pk)
        return Response({'detail': 'Contact deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    except Contact.DoesNotExist:
        logger.error('Contact with ID %d does not exist.', pk)
        return Response({'detail': 'Contact not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error('Error deleting contact with ID %d: %s', pk, str(e))
        return Response({'detail': 'An error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def list_contacts(request):
    logger.info('Received a request to list contacts.')
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    logger.info('Retrieved %d contacts.', len(serializer.data))
    return Response(serializer.data)
