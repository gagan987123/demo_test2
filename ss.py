"""
Sample Python file to test Autodoc Python integration
This file contains functions, classes, and variables for testing
"""

import os
import sys
from typing import List, Dict, Optional

# Global variables
API_VERSION = "v1.0"
MAX_RETRIES = 3
BASE_URL = "https://api.example.com"

# Configuration dictionary
config = {
    "timeout": 30,
    "debug": False,
    "log_level": "INFO"
}


def calculate_sum(a: int, b: int) -> int:
    """
    Calculate the sum of two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b


def process_data(data: List[Dict], filter_key: str = None) -> List[Dict]:
    """
    Process a list of dictionaries and optionally filter by key.
    
    Args:
        data: List of dictionaries to process
        filter_key: Optional key to filter by
        
    Returns:
        Processed list of dictionaries
    """
    if filter_key:
        return [item for item in data if filter_key in item]
    return data


async def fetch_user_data(user_id: int) -> Optional[Dict]:
    """
    Asynchronously fetch user data from API.
    
    Args:
        user_id: The ID of the user to fetch
        
    Returns:
        User data dictionary or None if not found
    """
    try:
        # Simulated API call
        user_data = {
            "id": user_id,
            "name": "John Doe",
            "email": "john@example.com"
        }
        return user_data
    except Exception as e:
        print(f"Error fetching user data: {e}")
        return None


class UserManager:
    """
    Manages user operations and data.
    """
    
    def __init__(self, database_url: str):
        """
        Initialize UserManager with database connection.
        
        Args:
            database_url: Database connection string
        """
        self.database_url = database_url
        self.users = {}
        self.active_sessions = []
    
    def add_user(self, user_id: int, username: str, email: str) -> bool:
        """
        Add a new user to the system.
        
        Args:
            user_id: Unique user identifier
            username: User's username
            email: User's email address
            
        Returns:
            True if user was added successfully, False otherwise
        """
        if user_id in self.users:
            return False
        
        self.users[user_id] = {
            "username": username,
            "email": email,
            "created_at": "2024-01-01"
        }
        return True
    
    def get_user(self, user_id: int) -> Optional[Dict]:
        """
        Retrieve user information by ID.
        
        Args:
            user_id: User identifier
            
        Returns:
            User dictionary or None if not found
        """
        return self.users.get(user_id)
    
    def delete_user(self, user_id: int) -> bool:
        """
        Delete a user from the system.
        
        Args:
            user_id: User identifier to delete
            
        Returns:
            True if deleted, False if user not found
        """
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False


class DataProcessor:
    """
    Processes and transforms data with various operations.
    """
    
    def __init__(self, config: Dict):
        self.config = config
        self.processed_count = 0
    
    def transform(self, data: List) -> List:
        """
        Transform data based on configuration.
        
        Args:
            data: Input data list
            
        Returns:
            Transformed data list
        """
        self.processed_count += len(data)
        return [item.upper() if isinstance(item, str) else item for item in data]
    
    def validate(self, data: Dict) -> bool:
        """
        Validate data structure.
        
        Args:
            data: Data dictionary to validate
            
        Returns:
            True if valid, False otherwise
        """
        required_keys = ["id", "name"]
        return all(key in data for key in required_keys)


# Utility function
def format_response(status: str, message: str, data: Optional[Dict] = None) -> Dict:
    """
    Format API response in standard structure.
    
    Args:
        status: Response status (success/error)
        message: Response message
        data: Optional data payload
        
    Returns:
        Formatted response dictionary
    """
    response = {
        "status": status,
        "message": message,
        "timestamp": "2024-01-01T00:00:00Z"
    }
    
    if data:
        response["data"] = data
    
    return response


# Main execution
if __name__ == "__main__":
    print("Sample Python file for Autodoc testing")
    
    # Test function calls
    result = calculate_sum(5, 10)
    print(f"Sum: {result}")
    
    # Test class instantiation
    manager = UserManager("postgresql://localhost/testdb")
    manager.add_user(1, "testuser", "test@example.com")
    
    # Test data processor
    processor = DataProcessor(config)
    transformed = processor.transform(["hello", "world"])
    print(f"Transformed: {transformed}")
