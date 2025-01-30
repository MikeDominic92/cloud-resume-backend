import pytest
from unittest.mock import Mock, patch
import json
from main import visitor_count

@pytest.fixture
def mock_request():
    return Mock(method='GET')

@pytest.fixture
def mock_firestore():
    with patch('main.firestore.Client') as mock:
        yield mock

def test_visitor_count_increment(mock_request, mock_firestore):
    # Mock the Firestore document
    mock_doc = Mock()
    mock_doc.exists = True
    mock_doc.to_dict.return_value = {'count': 5}
    
    # Mock the transaction
    mock_transaction = Mock()
    mock_transaction.get.return_value = mock_doc
    
    # Mock the Firestore client
    mock_client = Mock()
    mock_client.transaction.return_value = mock_transaction
    mock_firestore.return_value = mock_client
    
    # Call the function
    response = visitor_count(mock_request)
    
    # Parse the response
    data = json.loads(response[0].get_data())
    
    # Verify the response
    assert response[1] == 200  # Status code
    assert data['count'] == 6  # Incremented count
    
def test_visitor_count_new_counter(mock_request, mock_firestore):
    # Mock the Firestore document
    mock_doc = Mock()
    mock_doc.exists = False
    
    # Mock the transaction
    mock_transaction = Mock()
    mock_transaction.get.return_value = mock_doc
    
    # Mock the Firestore client
    mock_client = Mock()
    mock_client.transaction.return_value = mock_transaction
    mock_firestore.return_value = mock_client
    
    # Call the function
    response = visitor_count(mock_request)
    
    # Parse the response
    data = json.loads(response[0].get_data())
    
    # Verify the response
    assert response[1] == 200  # Status code
    assert data['count'] == 1  # First visitor

def test_cors_preflight(mock_firestore):
    # Create a mock OPTIONS request
    mock_options_request = Mock(method='OPTIONS')
    
    # Call the function
    response = visitor_count(mock_options_request)
    
    # Verify the response
    assert response[1] == 204  # Status code
    assert response[2]['Access-Control-Allow-Origin'] == '*'
    assert response[2]['Access-Control-Allow-Methods'] == 'GET'
