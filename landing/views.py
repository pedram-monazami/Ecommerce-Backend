from rest_framework.generics import CreateAPIView, ListAPIView
from landing.models import Location, Contact
from landing.serializers import ContactSerializer, LocationSerializer
from landing.tasks import send_email_task


class LocationListView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ContactCreateView(CreateAPIView):
    """
    A view for contacting to specific location.
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def perform_create(self, serializer):
        target_location_email = serializer.validated_data['location'].contact_email
        send_email_task.delay(
            serializer.validated_data['subject'],
            serializer.validated_data['content'],
            serializer.validated_data['sender_email'],
            [target_location_email]
        )
        super().perform_create(serializer)
