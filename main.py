from google.cloud import firestore
from flask import jsonify
import functions_framework
from flask_cors import CORS

# Initialize Firestore client
db = firestore.Client()

@functions_framework.http
def visitor_count(request):
    """HTTP Cloud Function that manages a visitor counter.
    Args:
        request (flask.Request): The request object.
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
    """
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    # Get the counter document
    counter_ref = db.collection('visitors').document('counter')
    
    @firestore.transactional
    def update_in_transaction(transaction, counter_ref):
        counter = counter_ref.get(transaction=transaction)
        current_count = 1
        
        if counter.exists:
            current_count = counter.to_dict().get('count', 0) + 1
        
        transaction.set(counter_ref, {
            'count': current_count
        })
        
        return current_count

    # Create a transaction
    transaction = db.transaction()
    try:
        count = update_in_transaction(transaction, counter_ref)
        return jsonify({'count': count}), 200, headers
    except Exception as e:
        return jsonify({'error': str(e)}), 500, headers
