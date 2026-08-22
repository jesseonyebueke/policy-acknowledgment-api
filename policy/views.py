from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PolicyAcknowledgment


CURRENT_POLICY = {
    'version': '1.0',
    'content': 'By using this service, you agree to our terms and conditions.',
    'effective_date': '2026-06-01',
}


@api_view(['GET'])
def current_policy(request):
    """Return the policy version that users may currently acknowledge."""
    return Response(CURRENT_POLICY)


@api_view(['POST'])
def acknowledge(request):
    """Validate and persist a policy acknowledgement for audit purposes."""
    user_name = request.data.get('user_name')
    policy_version = request.data.get('policy_version')

    if not user_name or not policy_version:
        return Response(
            {'error': 'user_name and policy_version are required'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if policy_version != CURRENT_POLICY['version']:
        return Response(
            {'error': 'Invalid policy version'},
            status=status.HTTP_400_BAD_REQUEST,
        )

    acknowledgment = PolicyAcknowledgment.objects.create(
        user_name=user_name,
        policy_version=policy_version,
    )

    return Response(
        {
            'message': 'Policy acknowledged successfully',
            'user_name': acknowledgment.user_name,
            'policy_version': acknowledgment.policy_version,
            'acknowledged_at': acknowledgment.acknowledged_at,
        },
        status=status.HTTP_201_CREATED,
    )
